from user import *
import cv2
import tensorflow as tf



class Coach:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)

    def segment_image(self, image):
        # Preprocesar la imagen
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (256, 256))
        image = image.astype("float32") / 255.0

        # Realizar inferencia con el modelo
        pred_mask = self.model.predict(image[tf.newaxis, ...])[0]

        # Postprocesar la máscara de segmentación
        pred_mask = tf.argmax(pred_mask, axis=-1)
        pred_mask = pred_mask[..., tf.newaxis]
        pred_mask = tf.image.resize(pred_mask, (image.shape[0], image.shape[1]))

        # Aplicar la máscara a la imagen original
        segmented_image = cv2.bitwise_and(image, image, mask=pred_mask)
        segmented_image = cv2.cvtColor(segmented_image, cv2.COLOR_RGB2BGR)

        return segmented_image

    def segment_live_video(self):
        # Capturar el video desde la cámara
        cap = cv2.VideoCapture(0)

        while True:
            # Leer un fotograma del video
            ret, frame = cap.read()

            # Segmentar la imagen del fotograma
            segmented_image = self.segment_image(frame)

            # Mostrar la imagen segmentada en una ventana
            cv2.imshow("Segmented Image", segmented_image)

            # Esperar una tecla para salir
            if cv2.waitKey(1) == ord("q"):
                break

        # Liberar la cámara y cerrar la ventana
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':

    user = User("johndoe2", "johndoe2@example.com", 75, 168, 0.13)
    print("Usuario creado exitosamente!")

