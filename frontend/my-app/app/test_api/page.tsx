"use client";

import React, { useEffect, useState, useRef } from 'react';
import { json } from 'stream/consumers';

interface StockData {
    open: number,
    high: number,
    low: number,
    close: number,
    volume: number,
}

interface StatCardProps {
    title: string;
    value: number;
}

const STAT_DEF: { [key: string]: string } = {
    "Open": "The price when the first stock trade was made when the market opened.",
    "High": "The highest price the stock trade was at during this period.",
    "Low": "The lowest price the stock trade was at during this period.",
    "Close": "The price when the last stock trade was made before the market closed.",
    "Volume": "The total number of shares or contracts traded during the period."
}
const StatCard = ({ title, value }: StatCardProps) => {
    // Logic for Info Icon 
    const [isPopOverOpen, setisPopOverOpen] = useState(false);
    const popoverRef = useRef<HTMLDivElement>(null);
    const definition = STAT_DEF[title];

    // Close the info if clicking outside
    useEffect(() => {
        const handleClickOutside = (event: MouseEvent) => {
            if (popoverRef.current && !popoverRef.current.contains(event.target as Node)) {
                setisPopOverOpen(false);
            }
        };
        document.addEventListener("mousedown", handleClickOutside);
        return () => {
            document.removeEventListener("mousedown", handleClickOutside);
        };
    }, []);

    return (
        <div className="bg-white p-8 rounded-xl shadow-lg border-l-4 border-[#0b462e] relative"
        ref={popoverRef}>
            {/* Title */}
            <div 
                className="flex items-center cursor-pointer group mb-1"
                onClick={() => setisPopOverOpen(!isPopOverOpen)}
            >
                <h3 className="text-lg font-medium text-gray-500 mr-2 group-hover:underline">{title}</h3>
                {/* Info Icon */} 
                <svg className="w-5 h-5 text-gray-400 group-hover:text-blue-500 transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
            </div>

            {/* Display Info */}
            {isPopOverOpen && definition && (
                <div className="absolute z-20 w-full p-3 top-0 left-0 mt-14 ml-0 bg-gray-800 text-white text-xs rounded-lg shadow-2xl transform translate-y-full">
                    <p className="font-semibold mb-1 text-base">{title}:</p>
                    {definition}
                </div>
            )}

            <p className="text-4xl font-extrabold text-gray-900">{value}</p>
        </div>
    );
};

const StatsPage = () => {
    {/* User Input/Search Bar */ }
    const [searchQuery, setSearchQuery] = useState('');

    {/* Fetching data */ }
    const [stockData, setStockData] = useState<StockData | null>(null);

    {/* Loading/Error state */ }
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    {/* API Fetching Logic */ }
    useEffect(() => {
        // If search bar empty don't fetch
        if (!searchQuery) {
            setStockData(null);
            setError(null);
            return;
        }

        const fetchData = async () => {
            setIsLoading(true);
            setError(null);

            const BASE_URL = 'http://localhost:5000';

            const Ticker = searchQuery.toUpperCase();
            const Fields = "metric, mean, median, std, low, max";
            const Table = 'stocks';
            const Conditions = `ticker = '${Ticker}' AND metric IN ('open','high','low','close','volume')`;

            const url = `${BASE_URL}/extract/${encodeURIComponent(Table)}/${encodeURIComponent(Fields)}/${encodeURIComponent(Conditions)}/data`;

            console.log("Fetching:", url);

            try {
                const response = await fetch(url);

                if (!response.ok) {
                    throw new Error(`Server responded with status: ${response.status}`);
                }

                const jsonResponse = await response.json();
                console.log("API response:", jsonResponse);

                // ✅ This is the ONLY place you should call setStockData
                if (Array.isArray(jsonResponse) && jsonResponse.length > 0) {
                    const rows = jsonResponse as { metric: string; mean: number }[];

                    const stock: StockData = {
                        open: rows.find(r => r.metric === "open")?.mean ?? 0,
                        high: rows.find(r => r.metric === "high")?.mean ?? 0,
                        low: rows.find(r => r.metric === "low")?.mean ?? 0,
                        close: rows.find(r => r.metric === "close")?.mean ?? 0,
                        volume: rows.find(r => r.metric === "volume")?.mean ?? 0,
                    };

                    console.log("Mapped stockData:", stock);
                    setStockData(stock);
                } else {
                    setError(`No data found for ticker: ${Ticker}`);
                    setStockData(null);
                }
            } catch (err: any) {
                console.error("Fetch error:", err);
                setError(`Failed to fetch data: ${err.message}`);
                setStockData(null);
            } finally {
                setIsLoading(false);
            }
        };

        // run fetch
        fetchData();
    }, [searchQuery]); // dependent on search, rerun whenever search changes

    // set default to 0 if no data is loaded yet
    const displayData = stockData || { open: 0, high: 0, low: 0, close: 0, volume: 0 };

    return (
        <div className="bg-white min-h-screen flex flex-col items-center p-8 font-inter">
            <h2 className="text-3xl font-bold text-gray-900 mb-6">Stocks</h2>

            {/* Search Bar */}
            <input
                type="text"
                placeholder="Enter company"
                className="text-black w-full max-w-7xl max-w-6xl py-5 px-6 mb-4 border-1 border-black-300 rounded-lg shadow-sm 
                focus:ring-blue-500 focus:border-blue-500 transition-colors placeholder-black-700
                placeholder:italic text-xl"

                value={searchQuery}
                onChange={(character) => setSearchQuery(character.target.value)}
            />

            {/* Conditional Loading/Error msgs */}
            {/* {isLoading && (
                <p className="text-xl text-blue-600 mb-6 font-medium animate-pulse">
                    <span role="img" aria-label="loading">⏳</span> Loading data for **{searchQuery}**...
                </p>
            )} */}
            {/* {error && (
                <div className="bg-red-100 border-l-4 border-red-500 text-red-700 p-4 w-full max-w-6xl mb-6" role="alert">
                    <p className="font-bold">Fetch Error</p>
                    <p>{error}</p>
                </div>
            )} */}

            {/* Stat cards */}
            <div className="grid grid-cols-2 md:grid-cols-5 gap-6 max-w-7xl w-full">
                <StatCard title="Open" value={displayData.open} />
                <StatCard title="High" value={displayData.high} />
                <StatCard title="Low" value={displayData.low} />
                <StatCard title="Close" value={displayData.close} />
                <StatCard title="Volume" value={displayData.volume} />
            </div>
        </div>
    )
}

export default StatsPage;