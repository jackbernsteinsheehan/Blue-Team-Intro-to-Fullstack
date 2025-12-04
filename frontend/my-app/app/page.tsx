"use client";

export default function Page() {
  return (
    <div>
   

      {/* MAIN LAYOUT */}
      <div className="row">
        <div className="side"></div>

        <div className="main">
          <h1 className="main_header">《 Welcome to our page 》</h1>
          <h1 className="inbox_title">🟆 Please explore our website! 🟆</h1>

          <div className="main-box">
           As the onborading team part of OSC we worked together to show our coding and team readiness skills. This was a 10 week long project we began during the beginning of Fall term 2025 in hopes to prove our skills to OSC to contiune our jounrey to move on to cilent work our following term. Our team was split apart to work on different sides of the website, with half the team being assigned front end development and the other half working on back end development.
          </div>

          {/* FRONT END BOX */}
          <div className="side-box-blocking">
            <div className="side-box">
              <div className="inbox_title"> 🟆 What the front end did 🟆</div>
              <img
                src="/font_end.png"
                alt="Front end"
                className="img-detail"
              />
              <p>developed .tsx files to build our website by split the work between 3 people with each person being assigned one part of the website, we choose who wanted to work on the home, about us, and data page. From there, each person coding their own section of the website and at the end, we shared our files to combine our work.</p>
            </div>

            {/* BACK END BOX */}
            <div className="side-box">
              <div className="inbox_title">🟆 What the back end did 🟆</div>
              <img
                src="/back_end.png"
                alt="Back end"
                className="img-detail"
                
              />
              <p>Handled utilizing public APIs to fetch live stock data and store it using SQL while also implementing Flask API connections with Python to provide the data to front end.</p>
            </div>
          </div>
        </div>
      </div>

      {/* FOOTER */}
      <div className="footer">
        <h2>Footer</h2>
      </div>

      {/* STYLES */}
      <style jsx>{`

      .img-detail {
    
        text-align: center;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        display: block;
        margin: 0 auto;
        width: 30%;
        border-radius: 5px; /* <— rounder edges */
        transition: transform 0.25s ease; /* smooth animation */
        }

        .img-detail:hover {
          transform: translateY(-8px); /* moves image up */
          box-shadow: 0 6px 16px rgba(14, 27, 24, 0.49); /* blue glow on hover */
        }
          .side-box p {
            margin-top: 20px;  /* controls spacing between img + text */
          }

        .inbox_title{
        font-family: "Courier New", Courier, monospace;
          text-align: center;
          font-size: 20px;
          padding: 20px;
          font-weight: bold;
        }

        .main_header {
          text-align: center;
          font-size: 60px;
          padding: 20px;
          transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .main_header:hover {
          transform: scale(1.05);
          shadow: 0 6px 16px rgba(14, 27, 24, 0.49); 
          color: #1f7e42ff;
          font-weight: bold;
        }

        .title {
          margin: 0;
          font-size: 30px;
          color: #1fbe5c; /* green text */
        }

        .small-title {
          margin: 5px 0 0;
          font-size: 15px;
          color: #1fbe5c; /* green text */
        }

        .header {
          background-color: #0b462e; /* dark green */
          text-align: center;
          padding: 20px;
          font-weight: bold;
        }

        .header-box {
          display: inline-block;
          background-color: #abcbff; /* light blue */
          border-radius: 16px;
          box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
          padding: 20px 40px;
          margin-bottom: 10px;
        }

        .navbar {
          overflow: hidden;
          background-color: #1d2c24;
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
          flex: 1;
          max-width: 70%;
          display: flex;
          justify-content: center;
          gap: 30px;       /* space between boxes */
          flex-wrap: wrap; /* prevents breaking on small screens */
          margin-top: 20px;
          text-align: center;
          display: block;
          background-color: #f1f1f1;
          border-radius: 16px;
          box-shadow: 0 4px 12px rgba(0,0,0,0.2);
          padding: 20px 40px;
          margin: 20px auto 0;
          color: black;
        }

        .side-box {
          flex: 1;
           max-width: 45%;
          text-align: center;
          display: inline-block;
          width: 45%;
          background-color: #f1f1f1;
          border-radius: 16px;
          box-shadow: 0 4px 12px rgba(0,0,0,0.2);
          padding: 20px 40px;
          margin: 20px 2.5%;
          color: black;
          vertical-align: top;
        }
        
        .side-box-blocking {
          display: flex;
          justify-content: center;
          gap: 30px;       /* space between boxes */
          flex-wrap: wrap; /* prevents breaking on small screens */
          margin-top: 20px;
        }


        .footer {
          background-color: #1d2c24;
          color: white;
          text-align: center;
          padding: 10px;
        }
      `}</style>
    </div>
  );
}
