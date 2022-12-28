
set -x #echo on

echo "Building user"
docker build . &> build.log
variableA=$(cat build.log | grep "writing image sha256" | cut  -d ':'  -f 2 | cut -d ' ' -f 1  )
echo "$variableA"

docker tag $variableA  909007/user:latest
docker push  909007/user:latest
echo "user Pushed  to docker"
cd manifests
kubectl delete -f ./
kubectl apply -f ./
echo "user Deployed"
cd ..
cd ..
