'use client'; // REQUIRED for useState and useEffect in Next.js App Router

import React, { useState, useEffect } from 'react';

// Helper function to generate a random number within a range
const getRandomNumber = (min: number, max: number, decimals: number = 2) => {
    const str = (Math.random() * (max - min) + min).toFixed(decimals);
    return parseFloat(str);
};

// Function to simulate fetching a statistics object
const mockStockStats = () => {
    // Use a fixed seed for 'Mock' symbol for consistency
    const seed = Math.random() * 100;
    
    const getRand = (min: number, max: number, decimals: number = 2) => {
        // Simple seeded variation for demonstration
        const val = (Math.random() + seed / 100) * (max - min) / 2 + min;
        return parseFloat(val.toFixed(decimals));
    }

    return {
        symbol: "Mock",
        latestPrice: getRand(150, 200),
        volume: Math.round(getRand(500000, 2000000, 0)), // No decimals for volume
        changePercent: getRand(-5, 5),
        peRatio: getRand(10, 30),
        marketCap: getRand(100, 500) + "B", // Adding 'B' for billion
    };
};

// Function to generate mock historical data (30 days)
const mockHistoryData = (startPrice: number, days: number = 30) => {
    const data = [];
    let currentPrice = startPrice;
    let currentDate = new Date();
    currentDate.setDate(currentDate.getDate() - days);

    for (let i = 0; i < days; i++) {
        currentDate.setDate(currentDate.getDate() + 1);
        // Simulate small daily random fluctuations
        currentPrice += getRandomNumber(-2, 3);
        currentPrice = Math.max(100, currentPrice); // Prevent price crash
        
        data.push({
            date: currentDate.toLocaleDateString('en-US', { month: 'short', day: 'numeric' }),
            price: parseFloat(currentPrice.toFixed(2)),
        });
    }
    return data;
};

// Helper function to convert text to title case for display
const toTitleCase = (str: string) => {
    if (!str) return '';
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
};


const StockStatsPage = () => {
    interface StockData {
        symbol: string;
        latestPrice: number;
        volume: number;
        changePercent: number;
        peRatio: number;
        marketCap: string;
    }
    
    const [data, setData] = useState<StockData | null>(null); 
    const [history, setHistory] = useState<{ date: string, price: number }[]>([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const timer = setTimeout(() => {
            const mockData = mockStockStats();
            const mockHistory = mockHistoryData(mockData.latestPrice * 0.9); // Start history below current price
            
            setData(mockData);
            setHistory(mockHistory);
            setLoading(false);
        }, 1500);

        return () => clearTimeout(timer);
    }, []); 

    if (loading) return (
        <div className="flex items-center justify-center min-h-screen bg-white">
            <div className="text-center p-10 text-xl text-green-600">
                <svg className="animate-spin -ml-1 mr-3 h-8 w-8 text-green-500 inline-block" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Loading Mock Data...
            </div>
        </div>
    );
    
    if (!data || history.length === 0) return (
        <div className="text-center p-10 text-xl text-red-500 bg-white min-h-screen">
            Error generating mock data.
        </div>
    );

    const formattedSymbol = toTitleCase(data.symbol);
    const isPositiveChange = data.changePercent > 0;
    const changeColor = isPositiveChange ? 'text-green-600' : 'text-red-600';

    return (
        <div className="bg-white min-h-screen flex flex-col items-center p-8 font-inter">
            <div className="container max-w-6xl mx-auto">
                <h1 className="text-5xl font-extrabold mb-3 text-center text-gray-900 border-b-4 border-green-800 pb-3">
                    {formattedSymbol} Statistics
                </h1>
                
                {/* 30-DAY PRICE CHART */}
                <div className="w-full bg-white p-6 mb-10 rounded-xl shadow-2xl border-t-8 border-green-800">
                    <h2 className="text-3xl font-bold text-gray-800 mb-4">30-Day Price History</h2>
                    <StockLineChart history={history} isPositive={isPositiveChange} />
                </div>


                {/* Dashboard Grid */}
                <div className="grid grid-cols-2 lg:grid-cols-4 gap-6">
                    
                    {/* FEATURED CARD: Latest Price with Sparkline */}
                    <div className="lg:col-span-2 bg-green-50 p-8 rounded-xl shadow-xl border-l-4 border-green-800 transition-all duration-300">
                        <p className="text-xl font-medium text-gray-500 mb-2">Latest Price</p>
                        <div className="flex justify-between items-center mb-4">
                            <p className={`text-6xl font-extrabold text-gray-900`}>
                                ${data.latestPrice.toFixed(2)}
                            </p>
                            <span className={`text-2xl font-bold ${changeColor}`}>
                                {isPositiveChange ? '▲' : '▼'} {data.changePercent.toFixed(2)}%
                            </span>
                        </div>
                        
                        {/* The Sparkline in this card is now redundant but kept for demonstration */}
                        <svg viewBox="0 0 100 20" className="w-full h-12">
                            <path d="M0,15 L25,10 L50,15 L75,5 L100,10" fill="none" stroke={isPositiveChange ? "#38a169" : "#ef4444"} strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"/>
                            <circle cx="100" cy="10" r="2" fill={isPositiveChange ? "#38a169" : "#ef4444"}/>
                        </svg>

                    </div>
                    
                    {/* GENERAL STAT CARDS */}
                    <StatCard title="Volume" value={data.volume.toLocaleString()} />
                    <StatCard 
                        title="Change (%)" 
                        value={`${data.changePercent.toFixed(2)}%`} 
                        isPositive={isPositiveChange} 
                    />
                    
                    <StatCard title="P/E Ratio" value={data.peRatio.toFixed(2)} />
                    <StatCard title="Market Cap" value={`$${data.marketCap}`} />
                    <StatCard title="52 Week High" value={`$${(data.latestPrice * 1.1).toFixed(2)}`} /> 
                    <StatCard title="52 Week Low" value={`$${(data.latestPrice * 0.9).toFixed(2)}`} /> 

                </div>
            </div>
        </div>
    );
};

export default StockStatsPage;

// --- Helper Component for Display ---
const StatCard = ({ title, value, isPositive }: { title: string, value: string | number, isPositive?: boolean }) => {
    const colorClass = isPositive === true ? 'text-green-600' : isPositive === false ? 'text-red-600' : 'text-gray-900';
    const borderColor = isPositive === true ? 'border-green-800' : isPositive === false ? 'border-red-500' : 'border-green-800';
    
    return (
        <div className={`bg-white p-6 rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 border-l-4 ${borderColor}`}>
            <p className="text-md font-medium text-gray-500 mb-1">{title}</p>
            <p className={`text-3xl font-extrabold ${colorClass}`}>{value}</p>
        </div>
    );
};

// --- Interactive Stock Line Chart Component (Pure SVG) ---
const StockLineChart = ({ history, isPositive }: { history: { date: string, price: number }[], isPositive: boolean }) => {
    const [hoverPoint, setHoverPoint] = useState<number | null>(null);
    const [hoverCoords, setHoverCoords] = useState<{ x: number, y: number } | null>(null);

    // Adjusted left margin: 70 -> 80 to ensure Y-axis label doesn't overlap title
    const margin = { top: 10, right: 30, bottom: 55, left: 80 }; 
    const width = 800 - margin.left - margin.right;
    const height = 300 - margin.top - margin.bottom;

    // Data scaling (finding min/max for Y axis)
    const prices = history.map(d => d.price);
    const minPrice = Math.min(...prices) * 0.95;
    const maxPrice = Math.max(...prices) * 1.05;

    // Scales (simple linear scaling)
    const scaleX = (index: number) => (index / (history.length - 1)) * width;
    const scaleY = (price: number) => height - ((price - minPrice) / (maxPrice - minPrice)) * height;

    // Generate SVG path string (X-Y column data)
    const linePath = history.map((d, i) => {
        const x = scaleX(i);
        const y = scaleY(d.price);
        return `${i === 0 ? 'M' : 'L'}${x},${y}`;
    }).join(' ');

    const lineColor = isPositive ? "#10b981" : "#ef4444"; // Emerald-500 or Red-500

    // X-Axis Labels (Date) - Show start, middle, and end dates
    const numPoints = history.length;
    const dateLabels = [
        { x: scaleX(0), label: history[0].date },
        { x: scaleX(Math.floor(numPoints / 2)), label: history[Math.floor(numPoints / 2)].date },
        { x: scaleX(numPoints - 1), label: history[numPoints - 1].date },
    ];

    // Y-Axis Labels (Price) - Show min, middle, and max prices
    const priceLabels = [
        maxPrice.toFixed(2), 
        ((minPrice + maxPrice) / 2).toFixed(2), 
        minPrice.toFixed(2)
    ];

    // --- INTERACTIVITY LOGIC ---
    const handleMouseMove = (event: React.MouseEvent<SVGRectElement>) => {
        const svg = event.currentTarget.ownerSVGElement;
        if (!svg) return;

        // Get mouse coordinates relative to the SVG viewbox (0 to 800)
        const CTM = svg.getScreenCTM();
        if (!CTM) return;
        
        // Calculate point relative to the chart area (0 to width)
        const clientX = event.clientX;
        const clientY = event.clientY;
        const rect = svg.getBoundingClientRect();
        
        // Calculate the mouse X position within the chart area (0 to width)
        const mouseX = ((clientX - rect.left) / (rect.width / (width + margin.left + margin.right))) - margin.left;
        
        if (mouseX < 0 || mouseX > width) {
            setHoverPoint(null);
            return;
        }

        // Determine which data point the mouse is closest to
        const nearestIndex = Math.round(mouseX / width * (history.length - 1));
        
        // Calculate coordinates for the tooltip
        const x = scaleX(nearestIndex) + margin.left;
        const y = scaleY(history[nearestIndex].price) + margin.top;
        
        setHoverPoint(nearestIndex);
        setHoverCoords({ x, y });
    };

    const handleMouseLeave = () => {
        setHoverPoint(null);
    };

    return (
        <div className="relative">
            <svg viewBox={`0 0 ${width + margin.left + margin.right} ${height + margin.top + margin.bottom}`} className="w-full h-auto">
                <g transform={`translate(${margin.left},${margin.top})`}>
                    
                    {/* Y-Axis Line (The vertical legend line) */}
                    <line x1="0" y1="0" x2="0" y2={height} stroke="#d1d5db" strokeWidth="1" />

                    {/* Cartesian Grid (Horizontal lines) */}
                    {priceLabels.map((_, index) => {
                         // Determine the ratio for scaling: 0 (top/max), 0.5 (middle), 1 (bottom/min)
                        const ratio = index / (priceLabels.length - 1);
                        return (
                            <line 
                                key={index} 
                                x1="0" 
                                y1={height * ratio} 
                                x2={width} 
                                y2={height * ratio} 
                                stroke="#e5e7eb" 
                                strokeDasharray="4 4"
                            />
                        );
                    })}

                    {/* Line Path */}
                    <path 
                        d={linePath} 
                        fill="none" 
                        stroke={lineColor} 
                        strokeWidth="3" 
                        strokeLinecap="round" 
                        strokeLinejoin="round"
                    />

                    {/* Y-Axis Labels (Price Column) */}
                    {priceLabels.map((price, index) => (
                        <text 
                            key={index} 
                            x="-10" // Price values (closer to axis line)
                            y={height * (index / (priceLabels.length - 1))} 
                            textAnchor="end" 
                            alignmentBaseline="middle" 
                            className="text-xs fill-gray-600"
                        >
                            ${price}
                        </text>
                    ))}
                    
                    {/* Y-Axis Legend Title */}
                    <text 
                        x="-65" // Moved further left to avoid collision
                        y={height / 2} 
                        textAnchor="middle" 
                        transform={`rotate(-90, -65, ${height / 2})`}
                        className="text-sm font-semibold fill-gray-700"
                    >
                        Price
                    </text>


                    {/* X-Axis Labels (Date Column) */}
                    {dateLabels.map((item, index) => (
                        <text 
                            key={index} 
                            x={item.x} 
                            y={height + 20} 
                            textAnchor="middle" 
                            className="text-xs fill-gray-600"
                        >
                            {item.label}
                        </text>
                    ))}
                    
                    {/* X-Axis Legend Title */}
                    <text 
                        x={width / 2} 
                        y={height + 40} 
                        textAnchor="middle" 
                        className="text-sm font-semibold fill-gray-700"
                    >
                        Date
                    </text>


                    {/* X-Axis Line */}
                    <line x1="0" y1={height} x2={width} y2={height} stroke="#d1d5db" strokeWidth="1" />
                    
                    {/* --- INTERACTIVE ELEMENTS (Hover Point and Tooltip) --- */}
                    {hoverPoint !== null && history[hoverPoint] && hoverCoords && (
                        <>
                            {/* Vertical Hover Line */}
                            <line 
                                x1={scaleX(hoverPoint)} 
                                y1="0" 
                                x2={scaleX(hoverPoint)} 
                                y2={height} 
                                stroke="#9ca3af" 
                                strokeDasharray="2 2"
                            />
                            {/* Hover Circle */}
                            <circle
                                cx={scaleX(hoverPoint)}
                                cy={scaleY(history[hoverPoint].price)}
                                r="5"
                                fill="#fff"
                                stroke={lineColor}
                                strokeWidth="2.5"
                            />
                        </>
                    )}

                </g>
                
                {/* Invisible Rectangle for Mouse Events */}
                <rect 
                    x={margin.left} 
                    y={margin.top} 
                    width={width} 
                    height={height} 
                    fill="transparent"
                    onMouseMove={handleMouseMove}
                    onMouseLeave={handleMouseLeave}
                />
            </svg>
            
            {/* Tooltip Overlay (HTML element for styling ease) */}
            {hoverPoint !== null && history[hoverPoint] && hoverCoords && (
                <div
                    className="absolute z-10 p-2 bg-gray-900 text-white rounded-lg shadow-xl pointer-events-none transition-opacity duration-150"
                    style={{
                        // Position the tooltip box near the hover point
                        left: hoverCoords.x + 10, 
                        top: hoverCoords.y - 10,
                        transform: 'translateY(-100%)', // Shift up to align pointer with point
                    }}
                >
                    <p className="text-sm font-bold">Price: ${history[hoverPoint].price.toFixed(2)}</p>
                    <p className="text-xs text-gray-400">Date: {history[hoverPoint].date}</p>
                </div>
            )}
            
            <p className="absolute top-2 right-4 text-xs font-medium text-gray-500">
                Data Points: {numPoints}
            </p>
        </div>
    );
};