import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const sizeOfRooms = [19, 20, 34];
  const classrooms = sizeOfRooms.map((size) => new ClassRoom(size));
  return classrooms;
}
