// src/app/components/AboutUs.tsx
import React from "react";

type AboutUsProps = {
    title?: string;
};
const AboutUs: React.FC<AboutUsProps> = ({title = "About Us"}) => {
    return (
        <main className="min-h-screen flex flex-col items-center justify-center p-8 bg-gray-50 text-gray-800">
            {/* Header Section */}
            <section className="text-center mb-12 max-w-2xl">
                <h1 className="text-5xl font-bold mb-4">{title}</h1>
                <p className="text-lg text-gray-600">
                    We're a team of students at the University of Oregon who are passionate
                    about creating innovative technology and developing innovative solutions.
                </p>
            </section>

            {/* Mission Seection */}
            <section className="max-w-3xl mb-12 text-center">
                <h2 className="text-3xl font semibold mb-4">Our Mission</h2>
                <p className="text-gray-700 leading-relaxed">
                    Our mission is to support eachother as developers and teammates to 
                    empower eachother. We are working towards a project to implement our skills
                    as a team, and as individuals. 
                </p>
            </section>

            {/* Team Section */}
            <section className="max-w-5xl text-center">
                <h2 className="text-3xl font-semibold mb-6">Our Team</h2>
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
                    <div className="bg-white shadow-lg rounded 2-xl p-6">
                        <img
                            src="https://via.placeholder.com/150"
                            alt="Team Member 1"
                            className="mx-auto rounded-full mb-4"
                        />
                        <h3 className="font-bold text-xl mb-2"> Carla Lopez</h3>
                        <p className = "text-gray-500"> Front-end Developr</p>
                    </div>
                    <div className="bg-white shadow-lg rounded 2-xl p-6">
                        <img
                            src="https://via.placeholder.com/150"
                            alt="Team Member 2"
                            className="mx-auto rounded-full mb-4"
                        />
                        <h3 className="font-bold text-xl mb-2">Sasha Ostrow</h3>
                        <p className="text-gray-500"> Front-end Developer</p>
                    </div>
                    <div className="bg-white shadow-lg rounded 2-xl p-6">
                        <img
                            src="https://via.placeholder.com/150"
                            alt="Team Member 3"
                            className="mx-auto rounded-full mb-4"
                        />
                        <h3 className="font-bold text-xl mb-2">Raymond Chung</h3>
                        <p className="text-gray-500"> Front-end Developer</p>
                    </div>
                    <div className="bg-white shadow-lg rounded 2-xl p-6">
                        <img
                            src="https://via.placeholder.com/150"
                            alt="Team Member 4"
                            className="mx-auto rounded-full mb-4"
                        />
                        <h3 className="font-bold text-xl mb-2">Jack Bernstein-Sheehan</h3>
                        <p className="text-gray-500"> Back-end Developer</p>
                    </div>
                    <div className="bg-white shadow-lg rounded 2-xl p-6">
                        <img
                            src="https://via.placeholder.com/150"
                            alt="Team Member 5"
                            className="mx-auto rounded-full mb-4"
                        />
                        <h3 className="font-bold text-xl mb-2">Adriana Walls</h3>
                        <p className="text-gray-500"> Back-end Developer</p>
                    </div> 
                </div>
            </section>
        </main>
    );
};
export default AboutUs;
