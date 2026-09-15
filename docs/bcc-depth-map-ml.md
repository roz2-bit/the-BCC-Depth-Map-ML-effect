# BCC+ Depth Map ML setup and usage

## Installation and licensing

Obtain BCC+ from Boris FX and follow its official installation and licensing instructions. Use a version supported by the chosen After Effects release. This repository contains no BCC+ installer, binary, preset, model, or activation material.

## A safe shot workflow

1. Duplicate the source layer and label the duplicate `FX_DEPTHML`.
2. Apply BCC+ Depth Map ML to the duplicate using the effect controls exposed by your licensed version.
3. Start with a short, representative range and inspect the depth result at 100%.
4. Adjust only what the shot needs; record important settings in `examples/metadata.example.json`.
5. Isolate difficult regions with masks or a dedicated precomp while retaining the clean source.
6. Compare the treatment against the clean layer and a neutral grade.

Control names and capabilities can vary between BCC+ versions. Treat the values in this repository as descriptive examples, not importable presets. If a result is unstable, simplify the shot, improve source contrast where lawful, or use a manually authored mask rather than stacking untracked fixes.

## Review questions

- Does the depth ordering remain plausible through camera or subject motion?
- Are edges stable across adjacent frames?
- Are transparent, reflective, or fine-detail regions handled intentionally?
- Can another editor reproduce the result from the shot notes?
