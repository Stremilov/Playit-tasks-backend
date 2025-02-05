import json
from fastapi import HTTPException, status, Request
from pandas import read_excel
from src.core.schemas.tasks import ParseTasksResponse


class ExcelService:
    @staticmethod
    async def parse_shop(request: Request) -> ParseTasksResponse:
        """
        Парсит Excel-файл и возвращает данные в виде ParseTasksResponse.
        """
        # user = await verify_user_by_jwt(request)
        # if not user:
        #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Пользователь не найден")

        # file_path = os.path.join("data", "PlayIT")

        file_path = "PlayIT.xlsx"

        # Проверка, что файл имеет корректное расширение
        if not file_path.endswith(".xlsx" or ".xls"):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Unprocessable content",
            )

        # Чтение Excel-файла с данными листа 'Персонажи'
        exel_shop_df = read_excel(file_path, sheet_name="Персонажи")
        if exel_shop_df.empty:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Такой таблицы не существует",
            )

        json_data = exel_shop_df.to_json(orient="records")

        formatted_json_data = json.loads(json_data)
        if not formatted_json_data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ошибка при форматировании данных из таблицы",
            )

        return ParseTasksResponse(
            status=status.HTTP_200_OK,
            details="Данные получены напрямую из Excel файла.",
            data=formatted_json_data,
        )
