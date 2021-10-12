FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/sunghak2234/hackathonproject.git

WORKDIR /home/hackathonproject/

RUN pip install -r requirements.txt

RUN echo "django-insecure-cu+^-625*4d844i3eznf04@t1i9%a2a-c(7x8+m(h3my*!3qob" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]