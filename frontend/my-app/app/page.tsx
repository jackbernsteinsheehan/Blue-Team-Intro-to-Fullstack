"use client";

export default function Page() {
  return (
    <div>
   

      {/* MAIN LAYOUT */}
      <div className="row">
        <div className="side"></div>

        <div className="main">
          <h1 className="main_header">Welcome to our page</h1>

          <h2>
            Our mission is to bring data to you to examine through charts of
            stock data. Explore our website by checking out our About Us and
            Data pages.
          </h2>

          <div className="main-box">
            As students at the University of Oregon, we are members of OSC — a
            club dedicated to connecting students with real-world clients to
            create free, impactful software solutions and develop the next
            generation of talent. Our team was split into a back-end team and a
            front-end team who worked together on this project.
          </div>

          {/* FRONT END BOX */}
          <div className="side-box">
            <div className="inbox_title">What the front end did</div>
            <img
              src="/font_end.png"
              alt="Front end"
              className="img-detail"
            />
            <p>Worked on displaying the website</p>
          </div>

          {/* BACK END BOX */}
          <div className="side-box">
            <div className="inbox_title">What the back end did</div>
            <img
              src="/back_end.png"
              alt="Back end"
              className="img-detail"
              
            />
            <p>Worked on data</p>
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

        .inbox_title{
          text-align: center;
          font-size: 20px;
          padding: 20px;
          font-weight: bold;
        }

        .main_header {
          text-align: center;
          font-size: 60px;
          padding: 20px;
        }

        .main_header:hover {
          transform: scale(1.05);
          shadow: 0 6px 16px rgba(14, 27, 24, 0.49); /* blue glow on hover */
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
