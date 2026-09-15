# Asset manifest

The manifest is an inventory, not a media bundle. Add one row per source, font, LUT, or external dependency in your private production tracker.

| ID | Kind | License/source | Required by | Stored in repository? |
| --- | --- | --- | --- | --- |
| `SRC-001` | Example footage | Replace with your licensed source | AE | No |
| `PLUG-001` | BCC+ Depth Map ML | Boris FX license | AE | No |
| `FONT-001` | Example font | Replace with a redistributable/team-approved font | CapCut | No |
| `MUSIC-001` | Example music | Replace with cleared music | CapCut | No |

Do not commit a manifest containing secrets, download tokens, personal data, or proprietary files. The safe machine-readable counterpart is `examples/asset-manifest.example.yml`.
