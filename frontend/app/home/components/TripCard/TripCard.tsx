"use client";
import { TextField } from "@mui/material";
import {
  Globe,
  MoveRight,
  MapPin,
  Calendar,
  DollarSign,
  Users,
  Sparkles,
} from "lucide-react";
export default function TripCard() {
  const activities = [
    "Museums",
    "Hiking",
    "Concerts",
    "Restaurants",
    "Shopping",
    "Beaches",
    "Historical Sites",
    "NightLife",
    "Nature",
    "Adventure Sports",
  ];
  return (
    <>
      <div className="z-[1] flex flex-col w-[90%]  gap-[1.5rem] rounded-[1rem] items-center bg-white p-[5%] lg:w-[63%] lg:p-[2%] shadow-2xl  ">
        <div className="flex flex-col gap-[1.5rem] w-full  bg-white lg:flex-row">
          <div className="flex flex-col gap-[0.5rem] w-full items-center">
            <div className="w-[80%] text-[0.9rem] font-bold text-gray-600 flex gap-[0.5rem] lg:text-[1rem]">
              <MapPin className="text-blue-500" size={20} />
              Destination
            </div>
            <TextField
              className="w-[80%]"
              id="outlined-basic"
              label="Enter city or country.."
              variant="outlined"
            />
          </div>
          <div className="flex flex-col gap-[0.5rem] w-full items-center">
            <div className="w-[80%] text-[0.9rem] font-bold text-gray-600 flex gap-[0.5rem] lg:text-[1rem]">
              <DollarSign className="text-blue-500" size={20} />
              Budget per Person
            </div>
            <TextField
              className="w-[80%]"
              id="outlined-basic"
              label="Enter your budget.."
              variant="outlined"
            />
          </div>
        </div>
        <div className="flex flex-col w-full  gap-[1.5rem]  bg-white items-center lg:flex-row">
          <div className="flex flex-col gap-[0.5rem] w-full items-center">
            <div className="w-[80%] text-[0.9rem] font-bold text-gray-600 flex gap-[0.5rem] lg:text-[1rem]">
              <Calendar className="text-blue-500" size={20} />
              Number of Days
            </div>
            <TextField
              className="w-[80%]"
              id="outlined-basic"
              label="Enter number of days.."
              variant="outlined"
            />
          </div>
          <div className="flex flex-col gap-[0.5rem] w-full items-center">
            <div className="w-[80%] text-[0.9rem] font-bold text-gray-600 flex gap-[0.5rem] lg:text-[1rem]">
              <Users className="text-blue-500" size={20} />
              Travel Type
            </div>
            <div className="flex gap-[2%] w-[80%] flex-wrap gap-y-[0.5rem]  ">
              <div className="flex-1 flex justify-center  rounded-[0.3rem] p-[2%] rounded-[0.5rem] border-gray-200 border-[3px] hover:border-gray-300 lg:p-[3%]">
                Solo
              </div>
              <div className="flex-1 flex justify-center   rounded-[0.3rem] p-[2%] rounded-[0.5rem] border-gray-200 border-[3px] hover:border-gray-300 lg:p-[3%]">
                Friends
              </div>
              <div className="flex-1 flex justify-center   rounded-[0.3rem] p-[2%] rounded-[0.5rem] border-gray-200 border-[3px] hover:border-gray-300 lg:p-[3%]">
                Family
              </div>
              <div className="flex-1 flex justify-center  rounded-[0.3rem] p-[2%] rounded-[0.5rem] border-gray-200 border-[3px] hover:border-gray-300 lg:p-[3%]">
                Couple
              </div>
            </div>
          </div>
        </div>
        <div className="flex flex-col items-center w-full gap-[0.5rem]  ">
          <div className="w-[80%] flex gap-[0.5rem] text-gray-600 font-bold text-[0.9rem] lg:w-[90%]  lg:text-[1rem]">
            <Sparkles size={20} className="text-blue-500" />
            Preferred Activities
          </div>
          <div className="flex flex-wrap w-[80%] gap-[3%]  gap-y-[0.5rem]  lg:w-[90%] ">
            {activities.map((item, index) => (
              <button
                className={`basis-[48%]  p-[2%] rounded-[0.5rem] border-gray-200 border-[3px] hover:border-gray-300 lg:basis-[26%] lg:p-[1%]  ${
                  item == "Historical Sites" || item == "Adventure Sports"
                    ? "text-center"
                    : "flex justify-center items-center"
                }`}
                key={index}
              >
                {item}
              </button>
            ))}
          </div>
        </div>
        <button className="flex items-center justify-center bg-red-200 rounded-[0.5rem] p-[5%] w-[80%] gap-[3%] text-white bg-gradient-to-br from-sky-500 to-emerald-600 hover:bg-gradient-to-br hover:from-sky-600 hover:to-emerald-700 lg:p-[2%] lg:w-[41%]  ">
          <div className="flex items-center">
            {" "}
            <Globe />
          </div>

          <div className="font-semibold"> Start AI Trip Planning </div>
          <div className="flex items-center">
            {" "}
            <MoveRight />
          </div>
        </button>
      </div>
    </>
  );
}
