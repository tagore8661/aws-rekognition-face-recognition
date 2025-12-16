import boto3
import os

s3 = boto3.resource('s3')

BUCKET_NAME = "<BUCKET-NAME>"
IMAGE_DIR = "images"   # local images folder

# List of images and corresponding cricketer names
images = [
    ('image_01.jpg', 'Virat Kohli'),
    ('image_02.jpg', 'Virat Kohli'),
    ('image_03.jpg', 'Virat Kohli'),
    ('image_04.jpg', 'Mahendra Singh Dhoni'),
    ('image_05.jpg', 'Mahendra Singh Dhoni'),
    ('image_06.jpg', 'Mahendra Singh Dhoni'),
    ('image_07.jpg', 'Rohit Sharma'),
    ('image_08.jpg', 'Rohit Sharma'),
    ('image_09.jpg', 'Suresh Raina'),
    ('image_10.jpg', 'Suresh Raina'),
    ('image_11.jpg', 'Chris Gayle'),
    ('image_12.jpg', 'Chris Gayle'),
    ('image_13.jpg', 'AB de Villiers'),
    ('image_14.jpg', 'AB de Villiers'),
    ('image_15.jpg', 'Phil Salt'),
    ('image_16.jpg', 'Phil Salt')
]

# Upload images to S3
for image_name, full_name in images:
    local_path = os.path.join(IMAGE_DIR, image_name)

    with open(local_path, 'rb') as file:
        s3_object = s3.Object(BUCKET_NAME, f"images/{image_name}")
        s3_object.put(
            Body=file,
            Metadata={'FullName': full_name}
        )

    print(f"Uploaded {image_name} for {full_name}")
