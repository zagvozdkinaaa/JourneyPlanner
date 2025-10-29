import Image from "next/image";
import imageTRavel from "../../../../public/travel.avif";
export default function Body() {
  return (
    <>
      <div className="relative h-screen w-full ">
        <Image
          fill
          className="object-cover opacity-70"
          alt="Image"
          src={imageTRavel}
        />
      </div>
    </>
  );
}
