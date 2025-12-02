
"use client";




export default function Page() {
  return (
    
<div>
      <div className="header">
        <h1 className = "header-box">The Blue Team</h1>
        <h1 className = "title">OSC</h1>
        <p className = "small-title">Oregon Software Consulting Onborading Project</p>
      </div>

      <div className="navbar">
        <a href="#" className="active">Home</a>
        <a href="#">Link</a>
        <a href="#">Link</a>
        <a href="#" className="right">Link</a>
      </div>

      <div className="row">
        <div className="side">

        </div>
        
        <div className="main">
          <h1 className = "main_header"><p>Welcome to our page</p></h1>
          <h1><p> Our mission is to bring data to you to examine through charts of stock data. Explore our website by checking out our about us and data page.</p></h1>
          <h1 className = "main-box"><p>As students at the Univerty of Oregon we are members part of OSC, 
            a club dedicated to connecting students with real-world clients to create free, impactful software solutions and
            develop the next generation of talent. The students that worked on this website share the passion to learn more about software develpment. Our team was broken up into two parts.
            The back end team, and the front end team, who worked together to make this project possible.</p></h1>




      <div className="side-box">
      <p>what the front end did</p>
      <img src="/font_end.png" alt="Front end" style={{ width: "100%", borderRadius: "8px" }} />
      <p>worked on displaying the website</p>
    </div>

    <div className="side-box">
      <p>what the back end did</p>
      <img src="/back_end.png" alt="Back end" style={{ width: "100%", borderRadius: "8px" }} />
      <p>worked on data</p>
    </div>

      </div>
      </div>

      <div className="footer">
        <h2>Footer</h2>
      </div>

      <style jsx>{`

        .main_header{
          text-align: center;
          font-size: 60px;
          padding: 20px;
        }

        .title {
          color: #1fbe5cff; 
          font-size: 40px;
        }

        .small-title {
          color: #1fbe5cff; 
          font-size: 15px;
        }
          

        .header {
          background-color: #0b462eff; 
          padding: 20px;
          text-align: center;
          font-weight: bold;
        }

        .header-box {
          display: inline-block; /* allows box to size to content */
          background-color: #abcbffff; /* the inner box color */
          border-radius: 16px;
          box-shadow: 0 4px 12px rgba(0,0,0,0.2);
          padding: 20px 40px;   /* space inside the box */
        }

        .navbar {
          overflow: hidden;
          background-color:  #1d2c24ff;
        }

        .navbar a {
          float: left;
          display: block;
          color: white;
          text-align: center;
          padding: 14px 16px;
          text-decoration: none;
        }

        .navbar a.right {
          float: right;
        }

        .row {
          display: flex;
          margin: 20px 0;
        }



        .main {
          flex: 75%;
          background-color: #ddd;
          padding: 20px;
        }
          .main-box {
            text-align: center;
            display: black; 
            background-color: #f1f1f1ff;
            border-radius: 16px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            padding: 20px 40px;
            margin: 20px auto 0;
            color: black;
        }

        .side-box {
          text-align: center;
          display: inline-block;   /* sit next to each other */
          width: 45%;              /* fit two boxes in one row */
          background-color: #f1f1f1ff;
          border-radius: 16px;
          box-shadow: 0 4px 12px rgba(0,0,0,0.2);
          padding: 20px 40px;
          margin: 20px 2.5%;       /* space between boxes */
          color: black;
          vertical-align: top;
        }

        .footer {
          background-color: #1d2c24ff;
          color: white;
          text-align: center;
          padding: 10px;
        }
      `}</style>
    </div>
  );
}
