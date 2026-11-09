# M450 LU04.A02 - Skip und xfail

Verwenden Sie `xfail`, `pytest.raises`, `skip` und `skipif`, um auf
unterschiedliche Situationen zu reagieren.

Wiki: <https://wiki.bzz.ch/modul/m450/learningunits/lu04/aufgaben/skipif>

## Ausgangslage

`calculator.py` ist ein einfacher Taschenrechner mit der Funktion
`divide(a, b)`. Mit gezielten Tests prüfen wir, wie das Programm auf
ungewöhnliche Situationen reagiert. Der Programmcode muss **nicht** verändert
werden.

## Auftrag

Erstellen Sie die Testfälle gemäss den Kommentaren `# TODO ...` in
`test_main.py`. Führen Sie die Testfälle einzeln aus und prüfen Sie den Output
im Terminal. Führen Sie zuletzt alle Tests mit `pytest -v` aus und prüfen Sie
wiederum die Ausgaben.

## Lokal testen

```bash
pip install -r requirements.txt
pytest -v
python _run_pylint.py
```

## Bewertung

| Teil | Punkte |
| --- | --- |
| `test_success`, `test_invalid`, `test_zero_division` | 3 |
| `test_mark_skip`, `test_mark_skip_conditional`, `test_pytest_skip` (nur Rückmeldung) | 0 |
| Linting von `test_main.py` | 3 |
| **Total** | **6** |

## Abgabe

Die Abgabe erfolgt durch den Push ins GitHub-Repository. Jeder Push wird
automatisch bewertet.
