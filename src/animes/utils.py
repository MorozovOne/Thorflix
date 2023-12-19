import secrets


async def upload_logo(logo):
    logo_name = logo.filename
    split_logo = logo_name.split(".")[1]
    token_name_logo = secrets.token_hex(10) + "." + split_logo
    generated_name_logo = 'files/logos/' + token_name_logo
    content_logo = await logo.read()

    with open(generated_name_logo, "wb") as file:
        file.write(content_logo)

    return generated_name_logo



async def upload_cover(cover):
    cover_name = cover.filename
    split_cover = cover_name.split(".")[1]
    token_name_cover = secrets.token_hex(10) + "." + split_cover
    generated_name_cover = 'files/covers/' + token_name_cover
    content_cover = await cover.read()
    with open(generated_name_cover, "wb") as file:
        file.write(content_cover)

    return generated_name_cover



async def upload_poster(poster):
    poster_name = poster.filename
    split_poster = poster_name.split(".")[1]
    token_name_poster = secrets.token_hex(10) + "." + split_poster
    generated_name_poster = 'files/posters/' + token_name_poster
    content_poster = await poster.read()
    with open(generated_name_poster, "wb") as file:
        file.write(content_poster)

    return generated_name_poster