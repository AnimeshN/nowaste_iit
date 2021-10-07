import React from 'react'
import LineChart from './LineChart/LineChart';
import './LineCharts.css';
import {calcDailyData,sliceLaneData}from '../util';
export default function LineCharts({data, selLane}) {
    

    const selLaneData = sliceLaneData(data,selLane);
    const dryData = calcDailyData(selLaneData,'dry');
    const wetData = calcDailyData(selLaneData,'wet');
    const rejectedData = calcDailyData(selLaneData,'rejected');
    const totalData = calcDailyData(selLaneData,'total');

    return (
        <div className='linecharts'>
        <LineChart data={dryData} selLane = {selLane} category="Dry"/>
        <LineChart data={wetData} selLane = {selLane} category="Wet"/>
        <LineChart data={rejectedData} selLane = {selLane} category="Rejected"/>
        <LineChart data={totalData} selLane = {selLane} category="Total"/>
        </div>
    )
}
