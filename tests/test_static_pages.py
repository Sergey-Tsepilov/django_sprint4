def test_static_pages_as_cbv():
    try:
        from pages import urls
    except Exception as e:
        raise AssertionError(
            "Убедитесь, что в файле `pages/urls.py` нет ошибок. При его"
            f" импорте возникла ошибка:\n{type(e).__name__}: {e}"
        ) from e
    try:
        from pages.urls import urlpatterns
    except Exception as error:
        raise AssertionError(
            "Убедитесь, что в файле `pages/urls.py` задан список urlpatterns."
        ) from error
    try:
        from pages.urls import app_name
    except Exception as error:
        raise AssertionError(
            "Убедитесь, что в файле `pages/urls.py` определена глобальная"
            " переменная `app_name`, задающая пространство имён url для"
            " приложения `pages`."
        ) from error
    for path in urlpatterns:
        if not hasattr(path.callback, "view_class"):
            raise AssertionError(
                "Убедитесь, что в файле `pages/urls.py` маршруты статических"
                " страниц подключены с помощью CBV."
            )
