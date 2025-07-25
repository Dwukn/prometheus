<hr>
<h1><center> Android app that blocks nsfw images </center></h1>


- Runs as a foreground service using MediaProjection.
- Classifies screen content with a quantized TFLite model every few seconds.
- Blurs the screen via SYSTEM_ALERT_WINDOW when NSFW content is detected.
- Provides a toggle UI and a persistent detection counter
<br>
<hr>
<h2><center> Tech Stack(Notes): </center></h2>

- Python
- TensorflowLite
- Kotlin
- Android Native
- Use of System Call from android kernel for Optimization
