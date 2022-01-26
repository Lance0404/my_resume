# my_resume
* [pandoc resume example](https://mszep.github.io/pandoc_resume/)

### Prerequisites
* install [pandoc](https://pandoc.org/)
    ```sh
    sudo apt-get install pandoc context
    ```
* install [wkhtmltopdf](https://wkhtmltopdf.org/)
    ```sh
    # read usage
    wkhtmltopdf -H
    ```
### Demo

* from md to html5
    ```sh
    # most frequently used
    pandoc --standalone -c style.css --from markdown --to html -o lance_resume.html lance_resume.md
    ```

* from html to pdf
    ```sh
    wkhtmltopdf --enable-local-file-access lance_resume.html lance_resume.pdf
    ```