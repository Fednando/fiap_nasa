import requests

api_key = "cFTrCeeFZC8ZrclYt3lZshyP5FbdxwyAJ6sJW8NU"
name_camera = "mardi"
birthdate = "1981-03-26"
url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=birthdate&sol=800&camera={name_camera}&api_key={api_key}"

result = requests.get(url)

if result.status_code == 200:
  dataPhoto = result.json()

  photos = dataPhoto["photos"]
  if len(photos) > 0:
    photo = photos[0]
    img = photo["img_src"]

    print(f"O retorno da imagem é : {img}")
  else:
    print("Imagem não encontrada")
else:
  print("Erro desconhecido")
