# Medilab_API
# Django Aplications
* [Django Rest Framework](https://www.django-rest-framework.org/)

## athentication: 
### Comentarios:
* Añadir filtros, pagination y ordenamiento a los endpoints.


* BaseUser
* Doctor
* Company
* Backteriologyst
* otherUser

## appointments:
* Appointments

# Pendientes
* Google Auth
* Email Auth (Confirmación del email)
* Añadir user_permissions al modelo de usuarios
* Grupos y Permisos

# Paginación
* La idea es que desde el backend exista una paginación de 100, para no pasar todos los datos al frontend, y que el frontend se encargue de la paginación de 10 en 10 por ejemplo.

# Comentarios
* Por practicidad será mejor dejar todo el tema de los grupos y permisos para el final.

* Ciudad en appointments (Datos de la recepción) es la ciudad donde se atiende el paciente, en ese caso se escoge el tarifario específico de dicha ciudad, además el doctor se pone como "NO APLICA".

* Encuesta de satisfación y anuncio al ingreso.

* Una empresa en misión son sub-empresas.

* Trabajo offline que se sincroniza con el sistema cuando se tenga internet.

* (Quién firma) es el doctor que atendió al paciente, no el que se asigna en recpción. Se verificia según el usuario.

* Se debe tener un filtro para que el doctor pueda ver solo sus pacientes. (Al menos en el caso de brigadas) - Se puede hacer creando un usuario DOctor-Brigada y asignando los pacientes a dicho usuario.

* Preguntar sobre los paquetes y que tanto se relaciona con las tarifas. ¿Una empresa puede llegar a hacer un examen que no esté registrado en el tarifario?

* Preguntar si se debe tener el dato de la empresa que está atendiendo al paciente.

    * * created_at = models.DateTimeField(auto_now_add=True)
    * * updated_at = models.DateTimeField(auto_now=True)

* Obtener los códigos de Actividad económica de las empresas desde una API.