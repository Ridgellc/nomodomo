# Nomo Domo menu, transcribed from their menu images (nomodomo.com/menu, Oct 2026).
# Light copyedits only: sentence case, "Ambejack" -> "Amberjack", "egg plant" -> "eggplant".
MENU = [
 ("ramen", "Ramen", "ramen", "From bone to broth, every bowl is a culmination of time, patience, and the art of layering flavors.", [
  ("Sous-vide chicken yuzu shio", 19, "A light, fragrant chicken bone broth infused with Japanese yuzu and sea salt, enoki, watercress, radish sprout and ajitama egg. Bright, citrus-kissed, and restorative.", ""),
  ("Seared pork belly tonkotsu", 20, "A 19-hour creamy pork bone broth crafted from four distinct cuts of pork. Layered with oyster and wood ear mushrooms, scallion, carrot chips, ajitama egg, and mayu black garlic oil.", "19-hour broth"),
  ("Vegan matcha kale noodle", 20, "Aromatic matcha-oil creamy broth with Japanese eggplant, tofu, mushroom, tomatoes and seasonal greens. Clean, comforting, and purely plant-based.", "Plant-based"),
  ("Roasted duck breast truffle shoyu", 23, "Medium soy-based broth, oyster mushroom, spinach, ajitama egg, radish sprout. Umami forward with elegance.", ""),
 ]),
 ("starter", "Starter", "share", "", [
  ("Onsen egg", 11, "Ikura, nameko mushroom, oyster mushroom, light mirin dashi.", ""),
  ("Enoki chips", 12, "Delicate enoki mushrooms fried until golden. Crisp, airy, and umami packed.", ""),
  ("Berkshire pork gyoza", 10, "Berkshire pork and vegetables, pan-seared and served with soy vinegar. Crisped with intention.", ""),
  ("Grilled shishito pepper", 9, "Flash-grilled shishito peppers with sea salt and ponzu. Smoky and mild with a hint of surprise.", ""),
  ("Kuro edamame", 7, "Special black pod soybeans, lightly salted. A simple start that honors purity of flavor.", ""),
  ("Karaage chicken", 11, "Juicy marinated chicken, double-fried for a perfect crunch. Finished with lemon and wasabi mayo.", ""),
  ("Agedashi tofu nasi", 14, "Roasted eggplant served in hot dashi. Smoky, soft, and steeped in tradition.", ""),
 ]),
 ("salad", "Salad", "bowls", "", [
  ("Cucumber sunomono", 9, "A refreshing trio of cucumber, daikon, and carrot, dressed in soy-rice vinegar with sesame. Light, cooling, and sharp.", ""),
  ("Japanese watercress yuzu mayo", 8, "A light, refreshing watercress with a hint of sesame flavor.", ""),
  ("Nomo Caesar salad", 12, "Crisp romaine with yuzu-kissed Caesar dressing. Familiar yet unmistakably Japanese.", ""),
 ]),
 ("rice", "Rice", "rice", "", [
  ("Pork katsu", 19, "Panko pork cutlet with shredded cabbage on a bed of steamed rice. A hearty and comforting Japanese classic.", ""),
 ]),
 ("special", "Special", "bluefin", "", [
  ("Kanpachi kama", 15, "Broiled amberjack collar with sea salt, grated daikon radish, ponzu.", ""),
  ("Domo rolls", 14, "Spicy crab stick, avocado, crispy wonton, and cucumber wrapped in sushi rice and seaweed. Topped with sesame, masago, crispy noodles.", ""),
  ("Bluefin tuna rolls", 16, "Avocado, rice cracker, scallion, cucumber, wrapped in crisp dried seaweed.", ""),
  ("Hon maguro sashimi", 23, "Five pieces of bluefin tuna, prized for its buttery texture and refined flavor. A pure and elegant taste of Nagasaki.", "Nagasaki, Japan"),
  ("Hon maguro carpaccio", 23, "Delicately sliced bluefin tuna, dressed with yuzu, sesame oil and microgreens. Silky, light, and beautifully balanced.", "Nagasaki, Japan"),
  ("Hayashi rice (steak stew)", 22, "Slow-simmered beef in demi-glace sauce over rice: stewed beef, grilled carrots, potatoes, eggplant, mushroom. Japanese-style comfort.", ""),
 ]),
]

def render():
    tabs, panels, photos = [], [], []
    for i, (key, label, img, intro, items) in enumerate(MENU):
        sel = "true" if i == 0 else "false"
        tabs.append(f'<button role="tab" id="tab-{key}" aria-controls="panel-{key}" aria-selected="{sel}" tabindex="{0 if i == 0 else -1}">{label}<sup>{len(items)}</sup></button>')
        rows = []
        for name, price, desc, tag in items:
            t = f'<span class="tag">{tag}</span>' if tag else ""
            rows.append(f'<li><div class="row"><h4>{name}</h4><i aria-hidden="true"></i><span class="price"><span class="sr">$</span>{price}</span></div><p>{desc}</p>{t}</li>')
        lead = f'<p class="lead">{intro}</p>' if intro else ""
        hidden = "" if i == 0 else " hidden"
        panels.append(f'<div role="tabpanel" id="panel-{key}" aria-labelledby="tab-{key}" data-img="{i}"{hidden}>{lead}<ul>{"".join(rows)}</ul></div>')
        photos.append(f'<img src="img/{img}.webp" alt=""{" class=\"on\"" if i == 0 else ""}>')
    return "".join(tabs), "".join(panels), "".join(photos)

if __name__ == "__main__":
    import sys
    src, out = sys.argv[1], sys.argv[2]
    tabs, panels, photos = render()
    html = open(src).read().replace("{{TABS}}", tabs).replace("{{PANELS}}", panels).replace("{{PHOTOS}}", photos)
    open(out, "w").write(html)
