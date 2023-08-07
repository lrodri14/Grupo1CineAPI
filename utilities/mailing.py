import random
from django.core.mail import EmailMessage

# Define your functions here.


def enviar_correo_bienvenida(nombre, apellido, recipiente):
    # Funcion responsable del envio del correo de bienvenida de un nuevo usuario
    sujeto = 'Bienvenido a Cinepolis'
    mensaje = 'Estimado/a {} {}\n\n' \
              '¡Nos complace darte una cálida bienvenida a Cinepolis, tu destino único para una experiencia excepcional de ver películas! Gracias por elegir nuestra aplicación para ser tu compañero definitivo en todo lo relacionado con el cine. \n\n' \
              'En Cinepolis, nos esforzamos por ofrecerte un inolvidable viaje cinematográfico con una amplia selección de los últimos éxitos de taquilla, clásicos atemporales y cautivadoras películas independientes. Con nuestra interfaz amigable y funciones avanzadas, podrás navegar fácilmente por los horarios de funciones, reservar boletos e incluso explorar eventos especiales.'.format(nombre, apellido)
    de = 'larodriguez@uth.hn'
    email = EmailMessage(sujeto, mensaje, de, [recipiente])
    email.send()


def enviar_correo_verificacion(nombre, apellido, recipiente, id):
    # Funcion responsable del envio del correo de bienvenida de un nuevo usuario
    sujeto = 'Verifica tu identidad'
    mensaje = 'Estimado/a {} {},\n\n' \
              '¡Gracias por registrarte en Cinepolis! Para completar el proceso de registro, necesitamos verificar tu dirección de correo electrónico. \n\n'\
              'Por favor, utiliza el siguiente código de verificación para confirmar tu cuenta: \n\n' \
              'Código de Verificación: {}'.format(nombre, apellido, id)
    de = 'larodriguez@uth.hn'
    email = EmailMessage(sujeto, mensaje, de, [recipiente])
    email.send()


def enviar_correo_boletos(nombre, apellido, recipiente, id):
    # Funcion responsable del envio del correo de bienvenida de un nuevo usuario
    sujeto = 'Compra de Boletos'
    mensaje = 'Estimado/a {} {},\n\n' \
              'Esperamos que disfrutes cada momento en nuestras instalaciones, desde la increíble calidad de imagen y ' \
              'sonido hasta el ambiente acogedor que creamos para ti. Ya sea que estés disfrutando de una película con ' \
              'amigos, familiares o por tu cuenta, sabemos que vivirás una experiencia única y memorable.\n\n' \
              'Código de Factura: {}-{}'.format(nombre, apellido, id, random.randint(999999, 10000000))
    de = 'larodriguez@uth.hn'
    email = EmailMessage(sujeto, mensaje, de, [recipiente])
    email.send()


def enviar_correo_productos(nombre, apellido, factura, recipiente):
    # Funcion responsable del envio del correo de bienvenida de un nuevo usuario
    sujeto = 'Compra de Productos'
    mensaje = 'Estimado/a {} {},\n\n' \
              'En Cinepolis, queremos expresar nuestro más sincero agradecimiento por elegirnos para disfrutar de una ' \
              'experiencia cinematográfica única. Estamos encantados de que hayas confiado en nosotros para ser parte de ' \
              'tu entretenimiento y diversión. \n\n' \
              'Código de Factura: {}-{}'.format(nombre, apellido, factura, random.randint(999999, 10000000))
    de = 'larodriguez@uth.hn'
    email = EmailMessage(sujeto, mensaje, de, [recipiente])
    email.send()

