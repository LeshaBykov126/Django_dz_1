from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8081


class MyServer(BaseHTTPRequestHandler):

    def __get_html_content(self):
        file_path = "index.html"

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                html_content = file.read()
                return html_content
        except FileNotFoundError:
            print(f"Файл '{file_path}' не найден.")
            return None
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return None

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.__get_html_content()
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes(page_content, "utf-8"))  # Тело ответа


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
