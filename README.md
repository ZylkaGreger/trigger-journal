# Trigger-Journal · „Niemand werden"

Ein kleines, sehr privates Werkzeug, um Trigger behutsam zu erfassen und über die
Zeit Muster sichtbar zu machen — **ohne zu urteilen und ohne zu reparieren.**

> Was mich im Aussen stört, hat fast nichts mit dem Aussen zu tun
> und fast alles mit etwas in mir.

Gehört zum persönlichen Projekt **„Niemand werden"** von Peter & Myriam (über das
Loslassen von Identitäten, im Geiste von Michael Singer). Die Praxis: Immer wenn
ich denke „es liegt am Aussen", schreibe ich es auf und stelle eine einzige Frage —
**„Bist du sicher, dass es im Aussen liegt?"** Am Ende der Woche schaue ich, welche
Muster hochkamen.

## Die Haltung (bitte zuerst lesen)

- **Es gibt nichts zu fixen.** Beobachten, nicht reparieren. „Lass es raus."
- **Kein Judgment** — und niemals Self-Judgment verstärken. Darum gibt es hier
  bewusst **keine Streaks, keine Punkte, keine „gut/schlecht"-Bewertung.**
- **Einladende Fragen statt Antworten.** Der Ton endet auf einer offenen Frage.
- **Maximal privat.** Local-first. Nichts wird hochgeladen.

## Zwei Wege — gleiche Daten

Du kannst frei wählen, je nach Moment. Beide schreiben dasselbe Format.

### 1. Die App (einfach ausfüllen, auch am Handy)

Öffne **`app/index.html`** im Browser — Doppelklick genügt, kein Installieren,
kein Account, läuft offline.

- Felder ausfüllen (nur **Situation + Story** sind Pflicht, der Rest ist optional).
- Ist viel „Aussen" da und die Wende noch leer, taucht sanft die Einladung auf:
  *„Bist du sicher, dass es im Aussen liegt?"* — eine Einladung, keine Korrektur.
- **„Ablegen"** speichert lokal im Browser (localStorage). Nichts verlässt dein Gerät.
- **„Woche kopieren · für Claude"** legt einen fertigen, behutsamen Text in die
  Zwischenablage — den fügst du in Claude (App oder Code) ein und bekommst die
  wöchentliche Reflexion.
- **Export / Import (.json)** für Backups oder um deine Liste bewusst zu teilen.

> Am Handy: Datei z. B. über die Datei-App öffnen, oder das Repo via GitHub Pages
> bereitstellen (siehe unten) und die Seite zum Home-Bildschirm hinzufügen.

### 2. Das Terminal (Claude Code)

Wenn du Claude Code im geklonten Ordner öffnest, hast du zwei Commands:

- **`/trigger`** — ich führe dich behutsam durch einen Eintrag und speichere ihn
  als `entries/JJJJ-MM-TT-HHMMSS.json`. Du kannst auch einfach drauflos erzählen.
- **`/woche`** — ich lese die Einträge der letzten 7 Tage und mache die
  wöchentliche Reflexion: was hochkam, ein vermutetes Muster, eine offene Frage.
  Keine Lösung, kein Ratschlag. Das passiert komplett lokal im Gespräch — **keine
  API, kein Schlüssel, keine Cloud.**

### Die Linsen für die Mustererkennung

Beim Auswerten greife ich auf `reference/lenses.md` zurück — eine kuratierte
Sammlung von Deutungs-Linsen aus der Tradition, in der „Niemand werden" steht:
**Michael Singer** (*The Untethered Soul*) — der innere Mitbewohner, der Zeuge
dahinter, **Samskaras** (gespeicherte Energie; das Rückgrat für „derselbe
Ur-Trigger auf verschiedenen Oberflächen"), Loslassen — sowie verwandte Stimmen:
Ramana Maharshi („Wer bin ich?"), Byron Katie („Stimmt das wirklich?"), der
buddhistische *zweite Pfeil* (für den Meta-Trigger), Eckhart Tolles Schmerzkörper,
Tara Brachs RAIN als Tonfall. Alles als **Angebote zum Bemerken** — kein
Diagnostizieren, kein Fixen.

## Datenschutz — wie Teilen funktioniert

**Geteilt wird das Werkzeug, niemals deine Einträge.**

- `.gitignore` schliesst den Inhalt von `entries/` aus. Deine intimen Daten landen
  **nie** auf GitHub. Jede:r führt sein eigenes Journal lokal.
- App-Einträge liegen im localStorage des Browsers — auch die kommen nirgendwo hin.
- „Meine Liste geben" ist immer eine **bewusste** Handlung: in der App auf
  *Exportieren*, und die Datei z. B. über Signal weitergeben.

## Mit Myriam teilen (über deinen persönlichen GitHub)

1. Repo auf deinem **persönlichen** GitHub-Account anlegen (privat oder öffentlich —
   es enthält nur den Code, keine Einträge).
2. Diesen Ordner pushen (Befehle unten).
3. Myriam lädt das Repo herunter (oder „Code → Download ZIP") und öffnet
   `app/index.html`. Fertig.
4. Optional **GitHub Pages** aktivieren (Settings → Pages → Branch `main`, Ordner
   `/app`* ), dann ist die App unter einer URL erreichbar und handytauglich.

\* Alternativ `app/index.html` als `index.html` ins Wurzelverzeichnis legen, falls
Pages nur das Root oder `/docs` anbietet.

## Datenformat

Ein Eintrag (App und Terminal identisch):

```json
{
  "id": "2026-06-29-201433",
  "timestamp": "2026-06-29T20:14:33",
  "context": "arbeit | beziehung | familie | sonstiges",
  "trigger_aussen": "die Situation (das Aussen)",
  "story": "wem/was ich die Schuld gebe",
  "koerper": "Sensation, Ort",
  "emotion": "das Gefühl",
  "identitaet": ["berührte Rollen/Identitäten"],
  "reflexion_innen": "wo ist es in mir?",
  "meta_trigger": false
}
```

Ein echtes Beispiel (aus Folge 2) liegt in `examples/`.

## Aufbau

```
trigger-journal/
├─ app/index.html        # die UI zum Ausfüllen (eine Datei, offline)
├─ commands/             # /trigger und /woche für Claude Code
├─ reference/lenses.md   # Deutungs-Linsen (Singer u. a.) für die Mustererkennung
├─ entries/              # deine Einträge (per .gitignore NICHT geteilt)
├─ examples/             # ein Beispiel-Eintrag
└─ .claude-plugin/       # Plugin-Manifest
```

---

*Dies ersetzt keine Therapie. Es ist ein Werkzeug für Selbstreflexion und
Mustererkennung — eine Ergänzung, keine Behandlung.*
