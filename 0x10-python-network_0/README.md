# 0x10. Python - Network #0
Unlike what's written in the name of the project, this project is actually Bash scripting while `Python - Network #1` is in Python.

## [0-body_size.sh](./0-body_size.sh)
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
- The size must be displayed in bytes
- You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

## [1-body.sh](./1-body.sh)
Write a Bash script that takes in a URL, sends a `GET` request to the URL, and displays the body of the response
- Display only body of a `200` status code response
- You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

## [2-delete.sh](./2-delete.sh)
Write a Bash script that sends a `DELETE` request to the URL passed as the first argument and displays the body of the response
- You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

## [3-methods.sh](./3-methods.sh)
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.
- You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

## [4-header.sh](./4-header.sh)
Write a Bash script that takes in a URL as an argument, sends a `GET` request to the URL, and displays the body of the response
- A header variable `X-HolbertonSchool-User-Id` must be sent with the value `98`
- You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

## [5-post_params.sh](./5-post_params.sh)
Write a Bash script that takes in a URL, sends a `POST` request to the passed URL, and displays the body of the response
- A variable `email` must be sent with the value `test@gmail.com`
- A variable `subject` must be sent with the value `I will always be here for PLD`
- You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

## [100-status_code.sh](./100-status_code.sh)
Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
- You are not allowed to use any pipe, redirection, etc.
- You are not allowed to use `;` and `&&`
- You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000

## [101-post_json.sh](./101-post_json.sh)
Write a Bash script that sends a JSON `POST` request to a URL passed as the first argument, and displays the body of the response.
- Your script must send a `POST` request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request
- You have to use `curl`

Please test your scripts in the sandbox provided, using the web server running on port 5000

## [102-catch_me.sh](./102-catch_me.sh)
Write a Bash script that makes a request to `0.0.0.0:5000/catch_me` that causes the server to respond with a message containing `You got me!`, in the body of the response.
- You have to use `curl`
- You are not allow to use `echo`, `cat`, etc. to display the final result

Please test your script in the sandbox provided, using the web server running on port 5000
