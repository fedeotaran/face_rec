import face_recognition
import cv2
import numpy as np

# Captura el webcam
video_capture = cv2.VideoCapture(0)

# Carga las imagenes
obama_image = face_recognition.load_image_file("obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

biden_image = face_recognition.load_image_file("yo.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# Arrac con las caras y los nombres
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding
]
known_face_names = [
    "Obama",
    "Fede"
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Captura el frame de video
    ret, frame = video_capture.read()

    # Achica el frame de video a 1/4 para hacer el proceso de reconocimiento más rápido
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convierte la imagen de BGR color que usa OpenCV por RGB colo que usa face_recognition
    rgb_small_frame = small_frame[:, :, ::-1]

    # Solo procesa una sóla vez el frame
    if process_this_frame:
        # Busca todas las caras en la imagen de video y las encodea
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # Compara la cara y con las que sabemos que son conocidas.
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # Usa la cara con menos diferencia
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Muestra de resultado
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Vuelva a escalar las ubicaciones faciales ya que el marco que detectamos se ajustó a 1/4
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Dibuja un cuado alrededor de la cara
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Dibuja un label con el nombre asociado a la cara
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Dibuja el resultado de la imagen
    cv2.imshow('Video', frame)

    # Aprieta q en el teclado para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Suelta el manejador de la camara
video_capture.release()
cv2.destroyAllWindows()
