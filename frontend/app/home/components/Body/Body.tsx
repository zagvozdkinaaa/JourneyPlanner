import Image from "next/image";
import imageTRavel from "../../../../public/travel.avif";
import TripCard from "../TripCard/TripCard";
export default function Body() {
  return (
    <>
      <div className="relative min-h-screen w-full flex flex-col items-center gap-[2rem] pb-[30%]">
        <Image fill className="object-cover " alt="Image" src={imageTRavel} />
        <div className="absolute inset-0 bg-gradient-to-b from-white/80 via-white/70 to-white/50"></div>

        <div className=" z-[1] text-[2.7rem] font-bold text-center bg-gradient-to-br from-sky-500 to-emerald-600 bg-clip-text text-transparent max-w-[90%] lg:text-[5rem] lg:w-[60%] leading-[1.1]">
          AI-Powered Travel Planning Made Simple
        </div>
        <div className="z-[1] text-center max-w-[90%]  text-gray-600 text-[1.2rem] lg:text-[1.6rem] lg:w-[50%]">
          Create personalized trips with AI suggestions, interactive maps, and
          social inspiration
        </div>
        <TripCard />
      </div>
    </>
  );
}
