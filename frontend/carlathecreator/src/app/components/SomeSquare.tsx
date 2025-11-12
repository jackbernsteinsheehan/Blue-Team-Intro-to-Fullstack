"use client"; // Important for components in the app directory

import React from 'react';

interface SomeSquareProps {
  color: string;
  text: string;
}

const SomeSquare: React.FC<SomeSquareProps> = ({ color, text }) => {
  return (
    <div style={{ backgroundColor: color, width: 250, height: 250 }}>
      <h1>{text}</h1>
    </div>
  );
};

export default SomeSquare;
