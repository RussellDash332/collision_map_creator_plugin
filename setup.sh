sudo apt-get install protobuf-compiler
mkdir build
cd build
cmake ../
make
export GAZEBO_PLUGIN_PATH=$GAZEBO_PLUGIN_PATH:~/collision_map_creator_plugin/build
