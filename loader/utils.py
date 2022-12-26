def save_picture(picture):
    filename = picture.filename
    file_type = filename.split('.')[-1]

    if file_type not in ['jpg', 'jpeg', 'svg', 'bmp', 'gif']:
        return

    picture.save(f'/home/purechromas/PycharmProjects/lesson12_homeworka/uploads/{filename}')
    return f'uploads/{filename}'
