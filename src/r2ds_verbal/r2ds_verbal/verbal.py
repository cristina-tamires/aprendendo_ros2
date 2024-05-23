# pip install gTTS
from gtts import gTTS
# pip install openai-whisper
import whisper
import rclpy
from rclpy.node import Node
from rclpy.logging import LoggingSeverity


def main(args=None):
    # Inicializa o processo
    rclpy.init(args=args)
    
    # Controi o nó
    node = Node('no_simples')

    tts = gTTS('Oi, e ai mano?', lang = "pt", tld = 'com.br' )
    tts.save('src/hello.mp3')


    model = whisper.load_model("base")
    result = model.transcribe("hello.mp3", fp16=False)
    print(result["text"])

    # Destroi o nó 
    node.destroy_node()

    # Finaliza o processo
    rclpy.shutdown()


if __name__ == '__main__':
    main() 




