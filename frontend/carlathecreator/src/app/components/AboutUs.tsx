// src/app/components/AboutUs.tsx

import React from "react";

const AboutUs: React.FC = () => {
    return (
        <main className="min-h-screen flex flex-col items-center justify-center p-8 bg-gray-50 text-white-800">
            {/* Header Section */}
            <section className="text-center mb-12 max-w-2xl">
                <h1 className="text-5xl font-bold mb-4">About Us</h1>
                <div className="bg-white shadow-lg rounded-2xl p-6">
                  <p className="text-lg text-gray-800">
                    We are the Blue Team of OSC Onboarding Project. Our team consists of our front-end developers
                    and back-end developers. We are passionate about creating innovative technology and developing innovative solutions.
                  </p>
                </div>
            </section>

            {/* Mission Seection */}
            <section className="max-w-3xl mb-12 text-center">
                <h2 className="text-3xl font-semibold mb-6">Our Mission</h2>
                <div className="bg-white shadow-lg rounded-2xl p-6">
                  <p className="text-gray-800 leading-relaxed">
                    Our mission is to grow as aspiring software engineers while strengthening our skills 
                    and creating meaningful impact. Throughout this journey we have been able to grow and collaborate as a team 
                    to display our skils for the next step as software engineers at OSC. 
                  </p>
                </div>
            </section>

            {/* Team Section */}
            <section className="max-w-5xl mx-auto text-center mb-12">
                <h2 className="text-3xl font-semibold mb-6">Our Team</h2>

            {/* First team members in a grid */}
            <div className="grid grid-cols-1 sm:grid-cols-2  gap-8 mb-8">
              <div className="bg-white shadow-lg rounded-2xl p-6">
                <h3 className="font-bold text-xl mb-2">Carla Lopez</h3>
                <p className="text-gray-600">Front-end Developer</p>
              </div>
              <div className="bg-white shadow-lg rounded-2xl p-6">
                <h3 className="font-bold text-xl mb-2">Sasha Ostrow</h3>
                <p className="text-gray-600">Front-end Developer</p>
              </div>
              <div className="bg-white shadow-lg rounded-2xl p-6">
                <h3 className="font-bold text-xl mb-2">Raymond Chung</h3>
                <p className="text-gray-600">Front-end Developer</p>
              </div>
              <div className="bg-white shadow-lg rounded-2xl p-6">
                <h3 className="font-bold text-xl mb-2">Jack Bernstein-Sheehan</h3>
                <p className="text-gray-600">Back-end Developer</p>
              </div>
          </div>

            {/* Last team member centered */}
            <div className="flex justify-center">
              <div className="bg-white shadow-lg rounded-2xl p-6 w-80">
                <h3 className="font-bold text-xl mb-2">Adriana Walls</h3>
                <p className="text-gray-600">Back-end Developer</p>
         </div>
     </div>
    </section>
   </main>
  );
};
export default AboutUs;
