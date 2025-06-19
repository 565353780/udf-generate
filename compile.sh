if [ "$(uname)" = "Darwin" ]; then
  PROCESSOR_NUM=$(sysctl -n hw.physicalcpu)
elif [ "$(uname)" = "Linux" ]; then
  PROCESSOR_NUM=$(cat /proc/cpuinfo | grep "processor" | wc -l)
fi

export MAX_JOBS=${PROCESSOR_NUM}

pip uninstall udf-cpp -y

rm -rf ../udf-generate/build
rm -rf ../udf-generate/*.egg-info
rm ../udf-generate/*.so

bear -- python setup.py build_ext --inplace
mv compile_commands.json build

pip install .
