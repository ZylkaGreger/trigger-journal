# Trigger-Journal – Projektkontext für Claude Code

Diese Datei ist der dauerhafte Kontext für dieses Projekt. Bitte vor dem Bauen lesen.
Sie ist die Kurzfassung plus die nicht verhandelbaren Leitplanken. Details zum bereits Gebauten stehen in `README.md`, das Datenmodell zeigt `examples/`, die Deutungs-Linsen liegen in `reference/lenses.md`, die Erfassungs-/Reflexions-Logik in `commands/`.

## Worum es geht

Das Tool gehört zum persönlichen Projekt „Niemand werden" (Untertitel-Kandidat: „Keine Probleme, nur Erfahrungen") von Peter & Myriam. Es ist **kein** generischer Mood- oder Habit-Tracker.

Kern-Idee: Was mich im Aussen stört, liegt fast immer in mir. Wir hängen an Identitäten („ich bin ja nur…", „so bin ich halt"), unter denen eine Angst liegt. Es gibt einen tiefen Ur-Trigger, an den man nicht direkt herankommt; man arbeitet an dem, was heute an die Oberfläche kommt.

## Was gebaut wird

Ein privates **Trigger-Journal mit Mustererkennung**:
1. Schnelles Erfassen eines Trigger-Eintrags (Auslöser/„Aussen", Story, Körpersensation, Emotion, berührte Identität, optionale Wende „wo ist es in mir?").
2. Sanfte Rückfrage bei starker Aussen-Verankerung: „Bist du sicher, dass es im Aussen liegt?"
3. Mustererkennung über Zeit: wiederkehrende Auslöser, Identitäten, vermuteter gemeinsamer Ur-Trigger, Kontext, Meta-Trigger („aufregen über das Aufregen").
4. Wöchentliche Reflexion mit **einer offenen Frage**, keine To-do-Liste.

## Nicht verhandelbare Prinzipien (am wichtigsten)

- **Nicht fixen.** „Es gibt nichts zu fixen." Beobachten, nicht reparieren.
- **Kein Judgment**, niemals Self-Judgment verstärken. Keine Streaks/Scores, die Versagen suggerieren. Keine Gut/Schlecht-Bewertung von Einträgen.
- **Keine toxische Positivität, kein Therapie-Sprech, keine Diagnosen.**
- **Einladende Fragen statt Antworten.** Ton endet auf Fragen.
- **Maximal privat.** Sehr intime Daten. Local-first, lokal gespeichert, idealerweise verschlüsselt, kein Cloud-Zwang.

## Offene Entscheidungen (mit Peter klären, nicht still selbst entscheiden)

- Form: Claude-Code-Plugin/Skill? CLI? lokale Web-App? Mobile? (Schnelles Erfassen unterwegs ist wichtig.)
- Einzel- oder Paar-Modus (Idee: „wenn ich's streng haben will, geb ich meine Liste dir").
- KI lokal vs. Anthropic API.
- Speicher: lokal (SQLite/Dateien) vs. verschlüsselte Sync.

## Arbeitsweise

- Erst die kleinste lauffähige Version (Eintrag erfassen + wöchentliche Reflexion), dann Mustererkennung.
- Die Mustererkennung wird erst mit echten Einträgen über mehrere Wochen gut. Nicht verfrüht überbauen.
- Bei Unklarheit zu Form/Scope: fragen, nicht raten.

---

## Bereits entschieden & gebaut (Stand 2026-07-03)

*Ergänzt in Absprache mit Peter — hält den Stand fest, damit die „offenen Entscheidungen" oben nicht neu aufgerollt werden.*

- **Form:** Beides. (a) Lokale **Web-App** `app/index.html` (eine Datei, offline, localStorage) als niedrigschwellige UI, auch fürs Handy. (b) **Claude-Code-Commands** `/trigger` (erfassen) + `/woche` (Reflexion), liegen in `.claude/commands/` (laden beim Klonen) und gespiegelt in `commands/` + `.claude-plugin/` (optionale Plugin-Installation).
- **KI:** **Lokal**, kein API-Key, keine Cloud. Reflexion entsteht im Gespräch mit Claude bzw. per „Woche kopieren → in Claude einfügen".
- **Modus:** Erst **Einzel**; Teilen bewusst per Export („meine Liste geben"). Paar-Modus später (v2).
- **Speicher:** Lokal — App im Browser-localStorage, Terminal als JSON in `entries/`. Beide **dasselbe Format**. `/woche` liest auch App-Exporte.
- **Datenschutz:** `entries/` und `reflections/` sind per `.gitignore` ausgeschlossen — geteilt wird nur das Werkzeug, nie die Daten. Repo ist privat (`ZylkaGreger/trigger-journal`).
- **Mustererkennung:** greift auf `reference/lenses.md` zurück — Deutungs-Linsen aus der „Niemand werden"-Tradition (Michael Singer: innerer Mitbewohner, Zeuge, Samskaras, Loslassen; sowie Ramana, Byron Katie, der zweite Pfeil, Tolle, Tara Brach/RAIN, Teile/Rollen). Immer als Angebote zum Bemerken — kein Diagnostizieren, kein Fixen.
