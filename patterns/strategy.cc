#include <vector>

class AbsInterpolator {
public:
	virtual double interpolate(double x) const = 0;
};

class LinearInterpolator : public AbsInterpolator {
	LinearInterpolator(std::vector<double> const &xvec, std::std::vector<double> const &yvec);
	double interpolate(double x) const;
};

class SplineInterpolator : public AbsInterpolator {
	SplineInterpolator(std::vector<double> const &xvec, std::std::vector<double> const &yvec);
	double interpolate(double x) const;
};
