#Todo esto se puede ver en la web de reflex en hosting

FROM python:3.11

WORKDIR /app
COPY . .

ENV VIRTUAL_ENV=/app/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3.11 -m venv $VIRTUAL_ENV

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

#para que sea mas eficiente (solo arranca el backen porque tenemos alojado en sitios distintos el front y el back)
CMD reflex run --env prod --backend-only