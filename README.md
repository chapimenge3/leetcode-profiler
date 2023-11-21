# leetcode-profiler

Generate a nicely formatted leetcode solution of a developer from his profile and also fetch articles if he submitted in the solution.

## Installation

```bash
git clone https://github.com/chapimenge3/leetcode-profiler
```

## Usage

Before using it we need to provide LEETCODE SESSION. 

### How to get LEETCODE SESSION

1. Login to leetcode
2. Open developer tools(F12 or right click and inspect)
3. Go to Application tab(Chrome) or Storage tab(Firefox)
4. Click on Cookies > https://leetcode.com
5. Copy the value of `LEETCODE_SESSION`
6. run this command in the current terminal 
    
    ```bash
    export LEETCODE_SESSION=<value>
    ```
7. Now you can use the script using
    
    ```bash
    python3 main.py
    ```

**NOTE:** As of now the script only works if you provide the `LEETCODE_SESSION` in the same terminal. If you close the terminal you need to provide the `LEETCODE_SESSION` again.

## Demo

You can find the demo Generated files in [here](demo) or click `chapi` folder in the root directory.

The folder structure is as follows

```bash
├── username
|   ├── README.md
|   ├── solutions
|   |   ├── question
|   |   |   ├── solution.py
|   |   |   ├── README.md
|   |   |   ├── article.md(TODO)

```

## Known Issues

- [ ] Login the user using username and password
- [ ] Fetching the articles and adding it to the solution

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)