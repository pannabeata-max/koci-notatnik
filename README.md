# Koci Notatnik — demo Cloudflare Pages

Statyczny blog HTML + CSS. Brak bazy danych, cookies analitycznych i formularzy.

## Publikacja GitHub → Cloudflare Pages
1. Utwórz repozytorium na GitHubie, np. `koci-notatnik`.
2. Rozpakuj ZIP i dodaj **zawartość folderu** (nie sam folder) do repozytorium.
3. Cloudflare → Workers & Pages → Create application → Pages → Connect to Git.
4. Wybierz repozytorium i gałąź `main`. Framework preset: None. Build command: `exit 0`. Build output directory: `.` (root repo).
5. Kliknij Deploy. Strona dostanie adres `*.pages.dev`.

## SEO — po publikacji
- Ustal faktyczny adres projektu `https://NAZWA.pages.dev/`.
- Uzupełnij adresy kanoniczne i absolutne adresy JSON-LD, gdy ustalimy ostateczny URL.
- Dodaj sitemap.xml z poprawnymi adresami dopiero po wyborze adresu projektu.
- Zweryfikuj witrynę w Google Search Console.

## Modyfikacja testowa
Zmień tytuł w `index.html`, zapisz commit i obserwuj automatyczne wdrożenie w Cloudflare.

Uwaga: to demonstracyjny blog, a nie porady weterynaryjne.
