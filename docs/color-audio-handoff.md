# Color, audio, and export handoff

## Color

Agree on the working and delivery color space before rendering. Keep interpretation consistent from source import through AE and CapCut. View a test export on the intended device and note whether the delivery is SDR or HDR. Avoid embedding an undisclosed LUT or automatic conversion.

## Audio

Choose one authoritative sample rate (commonly 48 kHz for video) and keep channel layout documented. Check sync at the first frame, a mid-point, and the final frame. Keep dialogue, music, and effects separated until the final export when the delivery format permits.

## Handoff record

Record:

- project, shot, and version identifiers;
- source and master frame rate, dimensions, and duration;
- color-management and HDR/SDR choice;
- audio sample rate, channels, and peak/loudness target;
- AE render codec/container and handle policy;
- CapCut export codec/container and platform target;
- reviewer, date, and known limitations.

The values in `examples/export-settings.example.yml` are illustrative placeholders. Confirm requirements with the receiving platform or post-production team.
