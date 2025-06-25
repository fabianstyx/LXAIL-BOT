
---

✅ README.md — LXAIL Helper Bot

# 🤖 LXAIL Helper - Discord Bot

**LXAIL Helper** es un bot de Discord diseñado para anunciar automáticamente nuevas versiones del software **LXAIL** con changelog personalizable, directamente desde archivos locales (`changelog.txt` y `pending_update.txt`). Ideal para mantener informada a tu comunidad de desarrolladores o testers.

---

## 🧰 Características

- Comando `!updateLXAIL <versión>` para publicar manualmente una actualización.
- Monitor automático de `pending_update.txt` para anuncios automáticos.
- Soporte para changelogs largos (se divide en varios mensajes si es necesario).
- Comandos adicionales como `!status` y `!help_lxail`.
- Integración simple mediante archivos `.txt`.
- Compatible con Termux en Android.

---

## 📁 Estructura de archivos

Coloca estos archivos en la misma carpeta del bot:

LXAIL-BOT/ ├── bot.py                 # Código principal del bot ├── changelog.txt          # Contenido del changelog de la versión ├── pending_update.txt     # Activador de publicación automática ├── .env                   # Contiene el token del bot

---

## ⚙️ Instalación

1. **Clona el repositorio** (o descarga los archivos):

```bash
git clone https://github.com/tuusuario/LXAIL-BOT.git
cd LXAIL-BOT

2. Instala dependencias:



pip install -r requirements.txt

> Si no tienes requirements.txt, instala manualmente:



pip install discord.py python-dotenv

3. Crea el archivo .env y añade tu token:



DISCORD_TOKEN=TU_TOKEN_DEL_BOT

4. Crea archivos base:



echo "OFF" > pending_update.txt
touch changelog.txt


---

🚀 Uso

Comando manual

En Discord:

!updateLXAIL 1.2.0

Usará el contenido de changelog.txt y enviará el anuncio al canal configurado.


---

Publicación automática

Edita pending_update.txt y coloca el número de versión:

echo "1.2.0" > pending_update.txt

En segundos, el bot publicará la actualización y volverá a poner OFF.


---

🛠 Comandos disponibles

Comando	Descripción

!updateLXAIL <ver>	Publica una nueva versión de LXAIL
!status	Muestra estado del bot y archivos
!help_lxail	Muestra todos los comandos del bot



---

📌 Recomendaciones

Ejecuta el bot con python bot.py

Usa tmux o nohup si quieres dejarlo corriendo en segundo plano.

Asegúrate que los archivos .txt estén en la misma carpeta que bot.py.



---

📄 Licencia

Este proyecto es de uso personal o educativo. Puedes adaptarlo y reutilizarlo bajo atribución.


---

💬 Contacto

Desarrollado para uso interno por LXAIL System.
Soporte técnico: [Discord privado o mensaje directo].

---

### ✅ ¿Dónde colocarlo?

Guarda ese contenido como un archivo llamado `README.md` dentro de tu carpeta `LXAIL-BOT`.

---

¿Quieres que te genere también el `requirements.txt` o un script `.sh` para iniciar el bot fácilmente?

