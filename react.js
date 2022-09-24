function Header(){
    return(
        <header>
                <div>
                <nav className = "nav">
                    <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9Ii0xMS41IC0xMC4yMzE3NCAyMyAyMC40NjM0OCI+CiAgPHRpdGxlPlJlYWN0IExvZ288L3RpdGxlPgogIDxjaXJjbGUgY3g9IjAiIGN5PSIwIiByPSIyLjA1IiBmaWxsPSIjNjFkYWZiIi8+CiAgPGcgc3Ryb2tlPSIjNjFkYWZiIiBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPgogICAgPGVsbGlwc2Ugcng9IjExIiByeT0iNC4yIi8+CiAgICA8ZWxsaXBzZSByeD0iMTEiIHJ5PSI0LjIiIHRyYW5zZm9ybT0icm90YXRlKDYwKSIvPgogICAgPGVsbGlwc2Ugcng9IjExIiByeT0iNC4yIiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIi8+CiAgPC9nPgo8L3N2Zz4K" alt="react logo" width ="40px"/>
                </nav>
                <ul className = "nav-items">
                    <li>Pricing</li>
                    <li>About</li>
                    <li>Contats</li>
                </ul>
                </div>
            </header>
    )
}

function Footer() {
    return(
        <footer className ="footer">
                <h3>Anthony's development. All rights reserved.</h3>
        </footer>
    )
}

function Main() {
    return(
        <div>
            <h1>Here are some of the reasons i love learning React: </h1>
            <ul>
                <li>It gives me joying doing that</li>
                <li>I Knew right from day one that that is the beauty of web</li>
                <li>It's ease to learn</li>
                <li>I am more likely to get a developer job if i know react</li>
            </ul>
        </div>
    )
}

function ReasonsForReact(){
    return (
        <div className="Main">

            <Header/>
            <Main/>
            <Footer/>

        </div>
    )
}

ReactDOM.render(<ReasonsForReact/>,document.getElementById("route"))