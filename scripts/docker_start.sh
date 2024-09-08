docker run \
  -e GRADIO_SERVER_NAME=0.0.0.0 \
  -e GRADIO_SERVER_PORT=7860 \
  -p 7860:7860 \
  -it \
  ktem:1.0
