/*
Test program for profiling and optimization. Compile and run with:

g++ profiling.cc
./a.out

Program takes about 13s with n = 1e8.
*/

#include <cmath>
#include <vector>

#include <boost/random.hpp>
#include <boost/random/normal_distribution.hpp>

boost::random::mt19937 rng;
boost::normal_distribution<> nd(0.0, 1.0);
boost::variate_generator<boost::mt19937&, boost::normal_distribution<> > generateGaussian(rng, nd);

std::vector<double> generateRandomList(int n) {
	std::vector<double> values;
	for(int i = 0; i < n; ++i) {
		values.push_back(generateGaussian());
	}
	return values;
}

void getMoments(std::vector<double> const &v, double &mean, double &rms) {
	int n = v.size();
	double sum(0), sumSq(0);
	for(int i = 0; i < n; ++i) {
		sum += v[i];
		sumSq += v[i]*v[i];
	}
	mean = sum/n;
	rms = std::sqrt(sumSq/n - mean*mean);
}

void run(int n) {
	std::vector<double> v = generateRandomList(n);
	double mean,rms;
	getMoments(v,mean,rms);
	std::cout << "n = " << n << ", mean = " << mean << ", rms = " << rms << std::endl;
}

int main() {
	run(100000000);
}
