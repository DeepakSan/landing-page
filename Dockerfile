FROM python3:latest

RUN python -m pip install hatch

WORKDIR /app

COPY . .

EXPOSE 5000

RUN hatch env create

CMD ["hatch","run","dev:build"]