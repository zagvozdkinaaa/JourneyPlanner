import { MapPin, Home, Compass, Users, User } from "lucide-react";
import MenuMobileButton from "../MenuMobileButton/MenuMobileButton";
export default function Header() {
  return (
    <>
      <div className="flex  p-[3%] lg:p-[1%] bg-white">
        <div className="flex  gap-[2%] basis-[80%] lg:basis-[53%] items-center ml-[3%] lg:ml-[8%]">
          <MapPin
            size={35}
            className="text-white bg-gradient-to-br from-sky-500 to-emerald-600 p-[2%] rounded-[0.5rem] lg:p-[0.3rem]"
          />
          <div className="text-[1.5rem] flex items-center font-bold bg-gradient-to-br from-sky-500 to-emerald-600 bg-clip-text text-transparent">
            TravelAI
          </div>
        </div>
        <div className="lg:hidden">
          {" "}
          <MenuMobileButton />
        </div>

        <div className="flex hidden lg:flex gap-[1%] justify-start  basis-[46%] text-gray-600">
          <div className="flex items-center gap-[6%] basis-[19%] p-[1%]  hover:bg-sky-50 hover:text-sky-700 rounded-[0.5rem] justify-center">
            <Home size={18} />
            <button className="text-[1.1rem]  hover:text-sky-600 font-semibold">
              Home
            </button>
          </div>
          <div className="flex flex items-center basis-[30%] p-[1%]  gap-[3%] hover:bg-sky-50 hover:text-sky-700 rounded-[0.5rem] justify-center">
            <Compass size={18} />
            <button className="text-[1.1rem] font-semibold  hover:text-sky-600">
              Trip Builder
            </button>
          </div>
          <div className="flex flex items-center basis-[17%] gap-[6%] p-[1%] hover:bg-sky-50 hover:text-sky-700 rounded-[0.5rem] justify-center">
            <Users size={18} />
            <button className="text-[1.1rem] font-semibold  hover:text-sky-600">
              Feed
            </button>
          </div>
          <div className="flex flex items-center basis-[19%] p-[1%] gap-[6%] hover:bg-sky-50 hover:text-sky-700 rounded-[0.5rem] justify-center">
            <User size={18} />
            <button className="text-[1.1rem] font-semibold  hover:text-sky-600">
              Profile
            </button>
          </div>
        </div>
      </div>
    </>
  );
}
