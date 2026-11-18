#!/usr/bin/env python3
"""Crop supplied artwork into a configurable PNG token. Requires Pillow."""
from __future__ import annotations

import argparse
from pathlib import Path
from PIL import Image, ImageChops, ImageDraw, ImageOps

def parse_color(value: str) -> tuple[int, int, int, int]:
    try:
        value = value.removeprefix('#')
        if len(value) != 6:
            raise ValueError
        return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4)) + (255,)
    except ValueError as exc:
        raise argparse.ArgumentTypeError('Use a six-digit RGB hex color.') from exc

def make_token(source: Path, output: Path, size: int = 512, ring_width: int = 0,
               ring_color: tuple[int, int, int, int] = (128, 128, 128, 255),
               shape: str = 'circle', force: bool = False) -> None:
    if size < 8 or size > 8192 or not 0 <= ring_width < size // 2:
        raise ValueError('Size must be 8..8192; border must be nonnegative and less than half the size.')
    if shape not in ('circle', 'square'):
        raise ValueError('Shape must be circle or square.')
    if output.suffix.lower() != '.png':
        raise ValueError('Output must have a .png extension.')
    if source.resolve() == output.resolve():
        raise ValueError('Source and output must be different files.')
    if output.exists() and not force:
        raise FileExistsError('Output exists; select a new path or explicitly pass --force.')
    with Image.open(source) as original:
        portrait = ImageOps.fit(ImageOps.exif_transpose(original).convert('RGBA'),
                               (size - 2 * ring_width,) * 2, method=Image.Resampling.LANCZOS)
    def mask(width: int) -> Image.Image:
        result = Image.new('L', (width * 3,) * 2, 0)
        drawer = ImageDraw.Draw(result)
        box = (0, 0, width * 3 - 1, width * 3 - 1)
        (drawer.ellipse if shape == 'circle' else drawer.rectangle)(box, fill=255)
        return result.resize((width,) * 2, Image.Resampling.LANCZOS)
    canvas = Image.new('RGBA', (size,) * 2, (0, 0, 0, 0))
    if ring_width:
        frame = Image.new('RGBA', (size,) * 2, ring_color)
        frame.putalpha(mask(size))
        hole = Image.new('L', (size,) * 2, 0)
        hole.paste(mask(portrait.width), (ring_width, ring_width))
        frame.putalpha(ImageChops.subtract(frame.getchannel('A'), hole))
        canvas.alpha_composite(frame)
    portrait.putalpha(ImageChops.multiply(portrait.getchannel('A'), mask(portrait.width)))
    canvas.alpha_composite(portrait, (ring_width, ring_width))
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output, format='PNG', optimize=True)

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--size', type=int, default=512)
    parser.add_argument('--ring-width', type=int, default=0)
    parser.add_argument('--ring-color', type=parse_color, default=parse_color('808080'))
    parser.add_argument('--shape', choices=('circle', 'square'), default='circle')
    parser.add_argument('--force', action='store_true', help='Explicitly authorize replacing an existing output')
    args = parser.parse_args()
    try:
        make_token(args.source, args.output, args.size, args.ring_width, args.ring_color, args.shape, args.force)
    except (ValueError, OSError) as exc:
        parser.error(str(exc))
    print(f'Wrote {args.output} ({args.size}x{args.size} PNG, {args.shape}).')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
