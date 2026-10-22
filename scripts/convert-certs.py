from pathlib import Path
from PIL import Image

src = Path("diplomas")
dst = Path("public/certificates")
dst.mkdir(parents=True, exist_ok=True)

mapping = {
    "10034.jpg": "deadline-2025.webp",
    "10019.jpg": "arctf4.webp",
    "10017.jpg": "vsosh-ib.webp",
    "10036.jpg": "dano.webp",
    "10013.jpg": "kanikuly-cu.webp",
    "10018.jpg": "bolshie-vyzovy.webp",
    "10020.jpg": "innoctf.webp",
    "10035.jpg": "school-ctf.webp",
    "10022.jpg": "eshko.webp",
    "10033.jpg": "deadline-2026.webp",
    "10031.jpg": "reshys.webp",
    "10012.jpg": "municipal-ib.webp",
    "10015.jpg": "municipal-law.webp",
}

for src_name, dst_name in mapping.items():
    path = src / src_name
    if not path.exists():
        print("MISSING", src_name)
        continue
    im = Image.open(path).convert("RGB")
    w, h = im.size
    max_side = 1600
    if max(w, h) > max_side:
        scale = max_side / max(w, h)
        im = im.resize((round(w * scale), round(h * scale)), Image.Resampling.LANCZOS)
    out = dst / dst_name
    im.save(out, "WEBP", quality=78, method=6)
    print(f"{src_name} -> {dst_name} {im.size} {out.stat().st_size // 1024}KB")
