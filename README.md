# dvmn_api_4

## Установка
1. Клоинруйте проект командой `git clone` и перейдите в директорию проекта:
```bash
git clone https://github.com/d3rr0m/dvmn_api_4.git
```
```bash
cd dvmn_api_4
```
2. Установите виртуальное окружение.
```bash
python -m venv venv
```
3. Активируйте только что созданное виртуальное окружение.
```bash
$ source venv/bin/activate
```
либо
```bash
venv\Scripts\activate.bat
```
4. Установите необходимые пакеты
```bash
pip install -r requirements.txt
```


## Использование
`fetch_spacex_images.py` - загрузка фотографий запуска ракет компании SpaceX. Файлы сохраняются в папку `images`.
**Необязательные аргументы:**
`-launch_id ` - id запуска ракеты. Не все запуски имеют фото старта. Пример id с фото - `5eb87ce3ffd86e000604b336`. Если аргумент не указан будут загружены фото с последнего старта, если фото имеются.
