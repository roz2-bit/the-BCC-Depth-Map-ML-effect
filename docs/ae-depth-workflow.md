# After Effects depth workflow

This guide describes a repeatable structure; it does not replace Adobe or Boris FX documentation.

## 1. Prepare the project

Create a project at the delivery frame rate and resolution. Import only media you are licensed to use. Keep source footage, precomps, renders, and notes in separate bins that mirror `templates/project-structure/`.

Use a comp name such as `SC010_SHOT020_depth_v003`. Keep the source interpretation, frame rate, and color-management choice in the project metadata.

## 2. Build a reversible treatment

Duplicate the clean source layer before applying the BCC+ effect. Keep the clean layer disabled but available for comparison. Put the depth treatment in a named precomp, and use adjustment layers for secondary grading rather than destructively changing the source.

Make a short test range first. Review subject edges, hair, thin objects, reflections, and motion before committing to a long render. Document any manual masks or exclusions in the shot notes.

## 3. Review and render

Review at 100% and at delivery size. Check for edge halos, temporal instability, banding, and unexpected transparency. Render an intermediate master with handles when the CapCut editor needs editorial flexibility. Record the render settings in the metadata and handoff checklist.

Never put an `.aep` or plugin-generated preset in this repository. Store production project files in the team's approved private storage.
